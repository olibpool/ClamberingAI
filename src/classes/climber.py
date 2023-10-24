import pygame as pg
import yaml
import math

config = yaml.safe_load(open("../config/config.yml"))

class Climber:
    def __init__(self, right_shoulder_loc, left_shoulder_loc, right_hip_loc, left_hip_loc, color):
        self.right_shoulder_loc = right_shoulder_loc
        self.left_shoulder_loc = left_shoulder_loc
        self.right_hip_loc = right_hip_loc
        self.left_hip_loc = left_hip_loc
        self.right_shoulder_loc = right_shoulder_loc
        self.right_shoulder_loc = right_shoulder_loc
        self.color = color

        self.right_leg_length = config['bodypart_sizes']['leg']
        self.left_leg_length = config['bodypart_sizes']['leg']
        self.right_arm_length = config['bodypart_sizes']['arm']
        self.left_arm_length = config['bodypart_sizes']['arm']
        self.torso_length = config['bodypart_sizes']['torso']
        self.head_radius = config['bodypart_sizes']['head']
        
        self.right_leg_angle = 0
        self.left_leg_angle = 0
        self.right_arm_angle = 0
        self.left_arm_angle = 0
        self.torso_angle = 0
        
    def rotate_right_leg(self, angle):
        self.right_leg_angle = angle
        
    def rotate_left_leg(self, angle):
        self.left_leg_angle = angle
        
    def rotate_right_arm(self, angle):
        self.right_arm_angle = angle
        
    def rotate_left_arm(self, angle):
        self.left_arm_angle = angle
        
    def contract_right_leg(self, contraction_percentage):
        # number of pixels to contract
        pix = self.right_leg_length * contraction_percentage
        
        # calculate the new length of the leg
        self.right_leg_length = self.right_leg_length - pix
        
        # use trigonometry to calculate the new location of the right hip (the right leg is the hypotenuse)
        theta = self.right_leg_angle * math.pi / 180
        move_x = pix * math.sin(theta)
        move_y = pix * math.cos(theta)

        # calculate the new location of the right hip
        self.right_hip_loc = (self.right_hip_loc[0] + move_x, self.right_hip_loc[1] + move_y)
        
    def contract_right_arm(self, contraction_percentage):
        # number of pixels to contract
        pix = self.right_arm_length * contraction_percentage
        
        # calculate the new length of the arm
        self.right_arm_length = self.right_arm_length - pix
        
        # use trigonometry to calculate the new location of the right shoulder (the right arm is the hypotenuse)
        theta = self.right_arm_angle * math.pi / 180
        move_x = pix * math.sin(theta)
        move_y = pix * math.cos(theta)

        # calculate the new location of the right shoulder
        self.right_shoulder_loc = (self.right_shoulder_loc[0] + move_x, self.right_shoulder_loc[1] + move_y)
        
    def contract_left_leg(self, contraction_percentage):
        # number of pixels to contract
        pix = self.left_leg_length * contraction_percentage
        
        # calculate the new length of the leg
        self.left_leg_length = self.left_leg_length - pix
        
        # use trigonometry to calculate the new location of the left hip (the left leg is the hypotenuse)
        theta = self.left_leg_angle * math.pi / 180
        move_x = pix * math.sin(theta)
        move_y = pix * math.cos(theta)

        # calculate the new location of the left hip
        self.left_hip_loc = (self.left_hip_loc[0] + move_x, self.left_hip_loc[1] + move_y)
        
    def contract_left_arm(self, contraction_percentage):
        # number of pixels to contract
        pix = self.left_arm_length * contraction_percentage
        
        # calculate the new length of the arm
        self.left_arm_length = self.left_arm_length - pix
        
        # use trigonometry to calculate the new location of the left shoulder (the left arm is the hypotenuse)
        theta = self.left_arm_angle * math.pi / 180
        move_x = pix * math.sin(theta)
        move_y = pix * math.cos(theta)

        # calculate the new location of the left shoulder
        self.left_shoulder_loc = (self.left_shoulder_loc[0] + move_x, self.left_shoulder_loc[1] + move_y)


    def draw(self, surface):
        # draw the head
        pg.draw.circle(surface, self.color, (int(self.right_shoulder_loc[0]), int(self.right_shoulder_loc[1] - self.torso_length - self.head_radius)), self.head_radius)
        
        # draw the torso
        pg.draw.line(surface, self.color, self.right_shoulder_loc, self.left_shoulder_loc, 5)
        
        # draw the right arm
        pg.draw.line(surface, self.color, self.right_shoulder_loc, self.right_hip_loc, 5)
        
        # draw the left arm
        pg.draw.line(surface, self.color, self.left_shoulder_loc, self.left_hip_loc, 5)
        
        # draw the right leg
        pg.draw.line(surface, self.color, self.right_hip_loc, (self.right_hip_loc[0] + self.right_leg_length * math.sin(self.right_leg_angle * math.pi / 180), self.right_hip_loc[1] + self.right_leg_length * math.cos(self.right_leg_angle * math.pi / 180)), 5)
        
        # draw the left leg
        pg.draw.line(surface, self.color, self.left_hip_loc, (self.left_hip_loc[0] + self.left_leg_length * math.sin(self.left_leg_angle * math.pi / 180), self.left_hip_loc[1] + self.left_leg_length * math.cos(self.left_leg_angle * math.pi / 180)), 5)