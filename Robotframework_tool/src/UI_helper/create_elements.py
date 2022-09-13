from tkinter import *


class CreateElement:
    def create_entrie(self, frame_name, width_amount, text=False, state_value=0):
        if text != False:
            text_area = StringVar(frame_name, text)
        else:
            text_area = StringVar(frame_name)

        if state_value != 0:
            entry_object = Entry(frame_name, width=width_amount, state=state_value, textvariable=text_area)
        else:
            entry_object = Entry(frame_name, width=width_amount, textvariable=text_area)

        return entry_object

    def create_checkbox(self, frame_name, label_text, variable_type):
        check_box_object = Checkbutton(frame_name, text=label_text, variable=variable_type)
        return check_box_object
        
    def create_button(self, frame_name, label_text, height_value=False, width_value=False):
        if height_value != False:
            if width_value != False:
                button_object = Button(frame_name, text=label_text, height=height_value, width=width_value)
            else:
                button_object = Button(frame_name, text=label_text, height=height_value)
        else:
            if width_value != False:
                button_object = Button(frame_name, text=label_text, width=width_value)
            else:
                button_object = Button(frame_name, text=label_text)
        return button_object
        
    def create_label_frame(self, master_frame, frame_name, p_x=False, p_y=False):
        if p_x != False:
            if p_y != False:
                label_frame_object = LabelFrame(master_frame, text=frame_name, padx=p_x, pady=p_y)
            else:
                label_frame_object = LabelFrame(master_frame, text=frame_name, padx=p_x)
        else:
            if p_y != False:
                label_frame_object = LabelFrame(master_frame, text=frame_name, pady=p_y)
            else:
                label_frame_object = LabelFrame(master_frame, text=frame_name)
        return label_frame_object