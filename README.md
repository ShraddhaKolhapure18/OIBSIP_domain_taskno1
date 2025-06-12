1.Objectives:
    Objectives of BMI calculator are
    1.Assessing Weight Status
    2.Supporting Healthcare Professionals
    3.General Health Awareness

2.Steps performed
    1.Imported tkinter module which is necessary to create GUI interface
    2.Created main window using tk.Tk()
    3.Used grid_rowconfigure() and grid_columnconfigure() to control the behavior of rows and columns within a widget 
    4.Added widgets
    Labels :For heading and input instruction
    Entry widgets : TO enter weight and height using stringVar
    Used buttons like 
    Calulate: Calls calculate_bmi to calulate the BMI
    Reset: Clears result and input
    5.Calculation logic
    Converts input to float, height Centimeter(cm) to meter and uses BMI following formula 

  BMI=Weight(kg)/(Height(m))^2
    Evaluates category and sets color accordingly 
    6.Live Update Feature 
    trace_add  is used to automatically update when user gives input

3.Tools Used
    1.Python3
    2.Tkinter=Standard python GUI library

4.Outcome
    The output is a fully functional desktop GUI application that:
    Takes user input for height and weight.
    Automatically displays BMI and health category with color-coded feedback.
    Has a clean and responsive layout.
    Allows the user to reset inputs.
