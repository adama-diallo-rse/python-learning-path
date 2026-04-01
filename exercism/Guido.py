EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(portions):
    return PREPARATION_TIME * portions

def elapsed_time_in_minutes(portions, elapsed_bake_time):
    return preparation_time_in_minutes(portions) + elapsed_bake_time