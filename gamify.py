from re import match
from typing import Match


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
    cur_hedons = 0
    cur_health = 0
    tired = None
    cur_star = None
    star_offer_time = None
    cur_star_activity = None

    bored_with_stars = False

    last_activity = None
    last_activity_duration = 0

    cur_time = 0

    last_finished = -1000


def star_can_be_taken(activity):
    pass



def perform_activity(activity, duration):
    star_elegible = get_star_elegible(activity)

    if(star_elegible):
            if(activity == "running"):
                if not tired:
                    if duration < 10:
                        cur_hedons += (2+3)*10
                        cur_health += 3*duration
                    elif duration > 10 and duration < 180:
                        cur_hedons += (2+3)*10 + -2*(duration-10)
                        cur_health += 3*duration
                    else:
                        cur_hedons += (2+3)*10 + -2*(duration-10)
                        cur_health += 3*180 + 1*(duration-180)
                else:
                    if duration < 10:
                        cur_hedons += (2+3)*10
                        cur_health += duration*-2
                    elif duration > 10 and duration < 180:
                        cur_hedons += (2+3)*10 + -2*(duration-10)
                        cur_health += duration*-2
                    else:
                        cur_hedons += (2+3)*10 + -2*(duration-10)
                        cur_health += duration*-2
            elif(activity == "textbooks"):
                cur_health+=2*duration
                if not tired:
                    if duration <=20:
                        cur_hedons+=duration
                    else:
                        cur_hedons+=duration*-1
                else:
                    cur_hedons+=-2*duration
            else:
                return 





def get_star_elegible(activity):
    same_activity = (activity == cur_star_activity)
    correct_time = (cur_time==star_offer_time)
    return same_activity and correct_time and not bored_with_stars

def get_cur_hedons():
    return cur_hedons
    
def get_cur_health():
    return cur_health
    
def offer_star(activity):
    global star_offer_time, cur_star_activity
    print ("get star for: "+ activity)
    star_offer_time = cur_time
    cur_star_activity = activity


def most_fun_activity_minute():
    pass
    
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
    print(get_cur_hedons())            # -20 = 10 * 2 + 20 * (-2)             # Test 1
    print(get_cur_health())            # 90 = 30 * 3                          # Test 2           		
    print(most_fun_activity_minute())  # resting                              # Test 3
    perform_activity("resting", 30)    
    offer_star("running")              
    print(most_fun_activity_minute())  # running                              # Test 4
    perform_activity("textbooks", 30)  
    print(get_cur_health())            # 150 = 90 + 30*2                      # Test 5
    print(get_cur_hedons())            # -80 = -20 + 30 * (-2)                # Test 6
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            # 210 = 150 + 20 * 3                   # Test 7
    print(get_cur_hedons())            # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
    perform_activity("running", 170)
    print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10
    
    
