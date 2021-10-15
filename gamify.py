from re import match
from typing import Match
# tests


def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''

    # current totals for headons and health (int)
    global cur_hedons, cur_health
    # current time elapsed in minutes (int)
    global cur_time
    # last activity completed (string) and the duration of the last activity (int)
    global last_activity, last_activity_duration
    # (boolean) if user if bored with stars
    global bored_with_stars
    # time that the current star is offered at (int)
    global star_offer_time
    # an array containing all star offer times (array)
    global star_times
    # the current activity offered with star (string)
    global cur_star_activity
    # (boolean) if user is tired
    global tired
    # (int) time sice activity
    global time_since_activity
    # (int) total duration of consecutive runs
    global curr_run_duration
    time_since_activity = 120
    cur_hedons = 0
    cur_health = 0
    curr_run_duration = 0
    tired = None
    star_times = []

    star_offer_time = None
    cur_star_activity = None

    bored_with_stars = False

    last_activity = None
    last_activity_duration = 0

    cur_time = 0

    # global last_finished
    # last_finished = -1000


def perform_activity(activity, duration):
    """
    Updates the current totals for hedons and health
        Parameters:
            activity (string): the activity being completed
            duration (int): the length of activity being completed

    """
    global cur_hedons, cur_health, tired, cur_time, time_since_activity, last_activity, last_activity_duration, curr_run_duration
    star_elegible = int(star_can_be_taken(activity))
    tired = is_tired()
    if(activity == "running"):
        arr = do_run(duration, star_elegible)
        time_since_activity = 0
        curr_run_duration += duration
        cur_health += arr[0]
        cur_hedons += arr[1]
    elif(activity == "textbooks"):
        arr = do_textbook(duration, star_elegible)
        time_since_activity = 0
        curr_run_duration = 0
        cur_health += arr[0]
        cur_hedons += arr[1]
    elif(activity == "resting"):
        time_since_activity += duration
        curr_run_duration = 0
    else:
        return
    
    cur_time += duration


def do_textbook(duration, star_elegible):
    """
    Updates current headon and health totals for when the activty it textbooks
        Paramaters:
            duration (int): length of activity
            star_elegible (boolean): if a star can be taken
        Returns:
            cur_health (int): health gained from activity
            cur_headons (int): headons gained from activity
    """
    global tired, cur_time, time_since_activity, last_activity, last_activity_duration, curr_run_duration
    curr_run_duration = 0
    cur_health = 0
    cur_hedons = 0
    cur_health += 2*duration

    if not tired:
        if duration <= 20:
            # if activity duration is 10 or under apply star bonus for that time, 
            # if duration is more than 10 minutes only apply start bonus for 10 minutes
            cur_hedons += duration + \
                (3*duration*star_elegible if duration < 11 else 3*10*star_elegible)
        else:
            # star elegible will be 0 or 1 so if false no bonus is added
            cur_hedons += 10 + (duration-10)*-1 + (3*10*star_elegible)

    else:
        cur_hedons += -2*duration + \
                (3*duration*star_elegible if duration < 11 else 3*10*star_elegible)

    return cur_health, cur_hedons


def do_run(duration, star_elegible):
    """     
    Updates current headon and health totals for when the activty it running
        Paramaters:
            duration (int): length of activity
            star_elegible (boolean): if a star can be taken
        Return:
            cur_health (int): health gained from activity
            cur_headons (int): headons gained from activity
    
    """
    global tired, curr_run_duration, time_since_activity
    cur_hedons = 0
    cur_health = 0
    if not tired:  
        # star_elegible will be either 1 or 0 due to being boolean, so if false no bonus applied
        if duration < 10:
            cur_hedons += 2*duration + (3*star_elegible*duration)
            cur_health += 3*duration
        elif duration > 10 and duration < 180:
            cur_hedons += (2)*10+(3*star_elegible *
                                  10) + -2*(duration-10)
            cur_health += 3*duration
        else:
            cur_hedons += (2)*10+(3*star_elegible * 10) + -2*(duration-10)
            cur_health += 3*180 + 1*(duration-180)
    else:
        # if tired use current run duration + duratin to calculate headons
        if duration+curr_run_duration < 10:
            cur_hedons += (-2)*duration+(3*star_elegible*duration)
            cur_health += 3*duration

        elif duration+curr_run_duration > 10 and duration+curr_run_duration < 180:
            cur_hedons += (-2)*10+(3*star_elegible * 10) + -2*(duration-10)
            cur_health += 3*duration

        else:
            cur_hedons += (-2)*10+(3*star_elegible * 10) + -2*(duration-10)
            cur_health += ((duration+curr_run_duration)-180 * 1) + \
                (duration-(duration+curr_run_duration-180))*3
   
    return cur_health, cur_hedons


def is_tired():
    """
    Returns if user is tired

        Returns:
            is_tired (boolean): if the user is tired and thus have done activity in last 120 minutes
        
    """
    is_tired = time_since_activity <120
    return is_tired


def tired_of_stars():
    """
    updates bored_with_stars global varibale if user has been offered 3 stars within 3 hours
    """
    global star_times, bored_with_stars
    if bored_with_stars:
        return
    if(len(star_times) < 3):
        bored_with_stars = False
    else:
        if(star_times[len(star_times)-1] - star_times[len(star_times)-3] < 180):
            bored_with_stars = True


def star_can_be_taken(activity):
    """
    returns if the user can use a star
        Parameters:
            activity (string): the activity being completed
        Returns:
            boolean: if the user can take a star 
    """
    same_activity = (activity == cur_star_activity)
    correct_time = (cur_time == star_offer_time)
    tired_of_stars()
    return same_activity and correct_time and not bored_with_stars and not bored_with_stars


def get_cur_hedons():
    """
    returns current headon total

        Returns:
            cur_headons (int): the current headon total
    """
    return cur_hedons


def get_cur_health():
    """
    returns current health total

        Returns:
            cur_health (int): the current health total
    """
    return cur_health


def offer_star(activity):
    """
    updates global variables star_offer_time, cur_star_activity, star_times

        Parameters:
            activity (string): the activity the star is offered for
    """
    global star_offer_time, cur_star_activity, star_times    
    star_times.append(cur_time)
    star_offer_time = cur_time
    cur_star_activity = activity


def most_fun_activity_minute():
    """
    returns which activity would net the most headons if duration was one minute

        returns:
            (string): which is either "textbooks", "running", or "resting"
    """
    global tired
    tired = is_tired()
    # star_elegible = int(star_can_be_taken(activity))
    running_headons = None
    textbooks_headons = None
    running_headons = do_run(1, int(star_can_be_taken("running")))[1]
    textbooks_headons = do_textbook(1, int(star_can_be_taken("textbooks")))[1]
    if(textbooks_headons > running_headons and textbooks_headons > 0):
        return "textbooks"
    elif(running_headons > textbooks_headons and running_headons > 0):
        return "running"
    else:
        return "resting"


################################################################################
# These functions are not required, but we recommend that you use them anyway
# as helper functions


def get_effective_minutes_left_hedons(activity):
    '''Return the number of minutes during which the user will get the full
    amount of hedons for activity activity'''
    pass


def get_effective_minutes_left_health(activity):
    pass


def estimate_hedons_delta(activity, duration):
    '''Return the amount of hedons the user would get for performing activity
    activity for duration minutes'''
    pass


def estimate_health_delta(activity, duration):
    pass

################################################################################


if __name__ == '__main__':
    initialize()
    # offer_star("running")
    perform_activity("textbooks", 10)
    offer_star("running")
    perform_activity("textbooks", 10)
    offer_star("running")
    perform_activity("textbooks", 10)
    print(get_cur_hedons())
    offer_star("textbooks")
    perform_activity("textbooks", 1)
    print(get_cur_hedons())