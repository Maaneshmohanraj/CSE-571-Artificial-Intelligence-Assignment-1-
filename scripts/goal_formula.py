#!/usr/bin/env python3
# encoding: utf-8

__copyright__ = "Copyright 2022, AAIR Lab, ASU"
__authors__ = ["Abhyudaya Srinet", "Rushang Karia", "Naman Shah"]
__credits__ = ["Siddharth Srivastava"]
__license__ = "MIT"
__version__ = "1.3"
__maintainers__ = ["Pulkit Verma", "Naman Shah"]
__contact__ = "aair.lab@asu.edu"
__docformat__ = 'reStructuredText'


def get_goal_string(object_dict, obj_list, obj_loc_list, goal_list, 
    goal_loc_list,env):
    """
        Returns
        ========
            str:
                A generic goal condition that will place every object based on
                its type and size at the correct goal.
    """

    # Append your goal condition to this string.
    #
    # Below are a few hints to help you along the way:
    # =================================================
    #
    # You can print the parameters to help you in coming up with a generalized
    # goal condition.
    #
    # You can also look at the (:objects) and (:init) of problem.pddl to give
    # you an idea of where your goal string is going wrong.
    #
    # Keep in mind the subject type and sizes of the bins and the books must
    # match.
    #
    # High level plans do not need actual co-ordinates, rather they use the
    # high-level locations found in the parameters of this method.
    #
    # Finally, there exists a way to write the goal condition using universal
    # and existential quantifiers.
    #
    # Executing wrong plans on Gazebo might not give you the right execution!
    #
    # Remember that the two environments have unique objects, goals and predicates!
    
    goal_string = "(:goal (and\n"

    if env == "bookWorld":
        #TODO:
       
        for i in obj_list:
        	for j,m in zip(goal_list,range(len(goal_loc_list))):
        		if object_dict['object'][i]['size']== object_dict['goal'][j]['size'] and object_dict['object'][i]['obj_type']== object_dict['goal'][j]['obj_type']:
        			goal_string += "(Book_At %s %s)\n" %(i,goal_loc_list[m])
        			goal_string += "(Bin_At %s %s)\n" %(j,goal_loc_list[m])
        			goal_string += "(Book_Subject %s %s)\n" %(i,"_".join(object_dict['goal'][j]['obj_type'].split(" ")))
        			goal_string += "(Book_Size %s %s)\n" %(i,object_dict['goal'][j]['size'])
        			goal_string += "(Bin_Subject %s %s)\n" %(j,"_".join(object_dict['goal'][j]['obj_type'].split(" ")))
        			goal_string += "(Bin_Size %s %s)\n" %(j, object_dict['goal'][j]['size'])
        			goal_string += "(not (In_Basket %s))\n" %(i)
        			break
        
    elif env == "cafeWorld":
        #TODO:
        # Replace this with the correct goal for cafeWorld environment
        for i in obj_list:
        	for j,m in zip(goal_list,range(len(goal_loc_list))):
        		if object_dict['object'][i]['size']== object_dict['goal'][j]['size']and object_dict['object'][i]['obj_type']== object_dict['goal'][j]['obj_type']:
        			goal_string += "(Food_At %s %s)\n" %(i,goal_loc_list[m])
        			goal_string += "(Table_At %s %s)\n" %(j,goal_loc_list[m])
        			goal_string += "(Ordered %s %s)\n" %(j,object_dict['goal'][j]['obj_type'])
        			goal_string += "(Portion_Size %s %s)\n" %(i,object_dict['goal'][j]['size'])
        			goal_string += "(Food_Type %s %s)\n" %(i,object_dict['goal'][j]['obj_type'])
        			goal_string += "(Ordered_Portion %s %s)\n" %(j,object_dict['goal'][j]['size'])
        			goal_string += "(not (In_Basket %s))\n" %(i)
        			break
        			
    goal_string += "(Empty_Basket tbot3)\n"
    goal_string += "))\n"
    
    return goal_string
    
    
def sample_goal_condition(object_dict, obj_list, obj_loc_list, goal_list, 
    goal_loc_list):
    """
        Returns
        ========
            str:
                A generic goal condition that moves the robot to any one of
                the object locations.

        
        .. note ::

            You can replace the contents of get_goal_string() with the text below
            to get an idea of what is expected.
            
            The goal condition in the stock task here is VASTLY different from the
            expectation from you. Please review the homework documentation to identify
            your task.
            
            Here are some instructions to run this in Gazebo.
            1. Replace the content of get_goal_string() with this method.
            2. rosrun hw2 refinement.py \
                --objtypes <object types> \
                --objcount <number of objects> \
                --seed <seed>
            3. rosrun hw2 gazebo.py

            The generic goal condition here is to move the robot to a object location.
            
            The stock task below generates a generic goal condition that moves the
            robot to a random object location and this is independent of the total 
            number of locations and objects. 
            
    """

    import random
    assert len(obj_loc_list) > 0
    i = random.randint(0, len(obj_loc_list) - 1)
    
    goal_string = "(:goal (and "
    goal_string += "(Robot_At tbot3 %s)" % (obj_loc_list[i])
    goal_string += "))\n"
    
    return goal_string
