from re import match
from typing import Match
# tests


def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''

    global cur_hedons, cur_health

    global cur_time
    global last_activity, last_activity_duration

    global last_finished
    global bored_with_stars
    global star_offer_time
    global cur_star_activity
    global tired
    global time_since_activity
    global curr_run_duration
    time_since_activity = 120
    cur_hedons = 0
    cur_health = 0
    curr_run_duration = 0
    tired = None
    cur_star = None
    star_offer_time = None
    cur_star_activity = None

    bored_with_stars = False

    last_activity = None
    last_activity_duration = 0

    cur_time = 0

    last_finished = -1000


def perform_activity(activity, duration):
    global cur_hedons, cur_health, tired, cur_time, time_since_activity, last_activity, last_activity_duration, curr_run_duration
    star_elegible = int(star_can_be_taken(activity))
    tired = is_tired()
    if(activity == "running"):
        arr = do_run(duration, star_elegible)
        time_since_activity = 0
        curr_run_duration += duration
        cur_health+=arr[0]
        cur_hedons+=arr[1]
    elif(activity == "textbooks"):
        arr = do_textbook(duration, star_elegible)
        time_since_activity = 0
        curr_run_duration=0
        cur_health+=arr[0]
        cur_hedons+=arr[1]
    elif(activity == "resting"):
        time_since_activity += duration
        curr_run_duration=0
    else:
        return
    cur_time += duration
    
def do_textbook(duration, star_elegible):
    global tired, cur_time, time_since_activity, last_activity, last_activity_duration, curr_run_duration
    curr_run_duration=0
    cur_health=0
    cur_hedons=0
    cur_health += 2*duration

    if not tired:  # not tired if not tired or using star
        if duration <= 20:
                # if activity for 10 or under apply star bonus for that time if walked more than 10 only do start bonus for 10
            cur_hedons += duration + \
            (3*duration*star_elegible if duration <11 else 3*10*star_elegible)
        else:
                # star elegible will be either the star bonus or 0
            cur_hedons += 10 + (duration-10)*-1 + (3*10*star_elegible)

    else:    
        cur_hedons += -2*duration
    # time_since_activity = 0
    # curr_run_duration=0
    return cur_health, cur_hedons

def do_run(duration, star_elegible):
    global tired, curr_run_duration, time_since_activity
    cur_hedons=0
    cur_health=0
    if not tired:  # not tired if not tired or using star
        if duration < 10:
            cur_hedons += 2*duration + (3*star_elegible*duration)
            cur_health += 3*duration
        elif duration > 10 and duration < 180:
            cur_hedons += (2)*10+(3*star_elegible *
                                    10) + -2*(duration-10)
            cur_health += 3*duration
        else:
            cur_hedons += (2)*10+(3*star_elegible *10) + -2*(duration-10)
            cur_health += 3*180 + 1*(duration-180)
    else:

        if duration+curr_run_duration < 10:
            cur_hedons += (-2)*duration+(3*star_elegible*duration)
            cur_health += 3*duration

        elif duration+curr_run_duration > 10 and duration+curr_run_duration < 180:
            cur_hedons += (-2)*10+(3*star_elegible * 10) + -2*(duration-10)
            cur_health += 3*duration

        else:
            cur_hedons += (-2)*10+(3*star_elegible * 10) + -2*(duration-10)
            cur_health+=((duration+curr_run_duration)-180 * 1) + (duration-(duration+curr_run_duration-180))*3
    # time_since_activity = 0
    # curr_run_duration += duration
    return cur_health, cur_hedons


def is_tired():

    return time_since_activity < 120


def star_can_be_taken(activity):
    same_activity = (activity == cur_star_activity)
    correct_time = (cur_time == star_offer_time)
    return same_activity and correct_time and not bored_with_stars


def get_cur_hedons():
    return cur_hedons


def get_cur_health():
    return cur_health


def offer_star(activity):
    global star_offer_time, cur_star_activity
    print("get star for: " + activity)
    star_offer_time = cur_time
    cur_star_activity = activity


def most_fun_activity_minute():
    global tired
    tired = is_tired()
    # star_elegible = int(star_can_be_taken(activity))
    running_headons = None
    textbooks_headons = None
    running_headons = do_run(1, int(star_can_be_taken("running")))[1]
    textbooks_headons = do_textbook(1, int(star_can_be_taken("textbooks")))[1]
    if(textbooks_headons > running_headons and textbooks_headons >0):
        return "textbooks"
    elif(running_headons>textbooks_headons and running_headons>0):
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
    perform_activity("running", 30)
    # -20 = 10 * 2 + 20 * (-2)             # Test 1
    print(get_cur_hedons())
    # 90 = 30 * 3                          # Test 2
    print(get_cur_health())
    # resting                              # Test 3
    print(most_fun_activity_minute())
    perform_activity("resting", 30)
    offer_star("running")
    # running                              # Test 4
    print(most_fun_activity_minute())
    perform_activity("textbooks", 30)
    # 150 = 90 + 30*2                      # Test 5
    print(get_cur_health())
    # -80 = -20 + 30 * (-2)                # Test 6
    print(get_cur_hedons())
    offer_star("running")
    perform_activity("running", 20)
    # 210 = 150 + 20 * 3                   # Test 7
    print(get_cur_health())
    # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
    print(get_cur_hedons())
    perform_activity("running", 170)
    # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print(get_cur_health())
    # -430 = -90 + 170 * (-2)              # Test 10
    print(get_cur_hedons())
