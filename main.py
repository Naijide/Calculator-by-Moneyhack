from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import formulas
import conversion
import webbrowser

Builder.load_file('design.kv')

##############################
def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


class ImageButton(ButtonBehavior,Image):
    pass
###########################################

class HomeScreen(Screen):
    def switch_to_finance(self):
        self.manager.transition.direction = "left"
        self.manager.current = "finance_calc"
    def switch_to_calculatorScreen(self):
        self.manager.transition.direction = "left"
        self.manager.current = "calculatorScreen"
    def switch_to_measurement(self):
        self.manager.transition.direction = "left"
        self.manager.current = "measurement_screen"
    def switch_to_about_us(self):
        self.manager.transition.direction = 'left'
        self.manager.current = "about_us_screen"
    def switch_to_user_guide(self):
        self.manager.transition.direction  = 'left'
        self.manager.current = 'user_guide_screen'


class RootWidget(ScreenManager):
    pass 



###########################################
class FinanceCalc(Screen):
    def return_home(self):
        self.manager.transition.direction = "right"
        self.manager.current = "home_screen"

    def switch_to_mortgage(self):
        self.manager.transition.direction = "left"
        self.manager.current = "mortgage_calc"

    def switch_to_investment(self):
        self.manager.transition.direction = "left"        
        self.manager.current = "investment_calc"

class MortgageCalc(Screen):
    def back_to_finance(self):
        self.manager.transition.direction = "right"
        self.manager.current = "finance_calc"

    def back_to_home(self):
        self.manager.transition.direction = "right"
        self.manager.current = "home_screen"
    
    def calculate(self,hp,dp,r,t,pt):
        if is_number(hp) and is_number(dp) and is_number(r) and is_number(t) == True:
            if int(t) != 0:
                result = formulas.calc_monthly_payment(hp,dp,r,t,pt)
                display = "Your monthly mortgage payment is $%s." %str(round(result,2))
                self.ids.answer.text = display
            else:
                self.ids.answer.text = "Error, period cannot be 0."
        else:
            self.ids.answer.text = "Error, please check your inputs."


class InvestmentCalc(Screen):
    def back_to_finance(self):
        self.manager.transition.direction = "right"
        self.manager.current = "finance_calc"
    def switch_to_interest(self):
        self.manager.transition.direction = "left"
        self.manager.current = 'interest_calc'
    def switch_to_inflation(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'inflation_calc'
    def switch_to_pv(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'present_val_calc'


class InterestCalc(Screen):
    def back_to_investment(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'investment_calc'
    def back_to_home(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home_screen'
    
    def calculate(self,pri,r,t,mc,c):
        if is_number(pri) and is_number(r) and is_number(t) and is_number(mc) == True:
            if c != "Compounding Period":
                result = formulas.compound_interest(pri,r,t,mc,c)
                display = "Total Balance: $%s." %str(round(result,2))
                self.ids.answer.text = display
            else:
                self.ids.answer.text = "Please select compounding period"
        else:
            self.ids.answer.text = "Error, Please check your inputs."




class InflationCalc(Screen):
    def back_to_investment(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'investment_calc'
    def back_to_home(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home_screen'

    def calculate(self,price,rate,period):
        if is_number(price) and is_number(rate) and is_number(period) == True:
            result = formulas.calculate_inflation(price,rate,period)
            display  = "A price of ${0} will be ${1} after {2} years.".format(price, str(round(result,2)), period)
            self.ids.answer.text = display
        else:
            self.ids.answer.text = "Error, please check your inputs."


class PresentValCalc(Screen):
    def back_to_investment(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'investment_calc'
    def back_to_home(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home_screen'

    def calculate(self,fv,rate,period):
        if is_number(fv) and is_number(rate) and is_number(period) == True:
            result = formulas.present_val(fv,rate,period)
            display = "Present Value of ${0} after {1} years is ${2}.".format(fv,period,str(round(result,2)))
            self.ids.answer.text = display
        else:
            self.ids.answer.text = "Error, please check your inputs."






###########################################

class CalculatorScreen(Screen):
    def back_to_home(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home_screen'
    
    
    def calculate(self, calculation):
        if calculation:
            try:
                self.ids.entry.text = str(eval(calculation))
            except Exception:
                self.ids.entry.text = "Error"
            




###########################################

class MeasurementScreen(Screen):
    def return_to_home(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home_screen'
    def switch_to_length(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'length_screen'
    def switch_to_mass(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'mass_screen'
    def switch_to_volume(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'volume_screen'


class LengthScreen(Screen):
    def back_to_measurement(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'measurement_screen'
    def return_to_home(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home_screen'

    def calculate(self,l1,l2,input):
        if l1 != "Length 1" and l2 != "Length 2":
            if is_number(input):
                result = conversion.get_length_conversion(l1,l2,input)
                display = "{0} {1} is {2} {3}.".format(input,l1,str(result),l2)
                self.ids.answer.text = display
            else:
                self.ids.answer.text = "Error, please check input."
        else:
            self.ids.answer.text = "Please select units"


class MassScreen(Screen):
    def back_to_measurement(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'measurement_screen'
    def return_to_home(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home_screen'

    def calculate(self,m1,m2,input):
        if m1 != "Mass 1" and m2 != "Mass 2":
            if is_number(input):
                result = conversion.get_mass_conversion(m1,m2,input)
                display = "{0} {1} is {2} {3}.".format(input,m1,str(result),m2)
                self.ids.answer.text = display
            else:
                self.ids.answer.text = "Error, please check input."
        else:
            self.ids.answer.text = "Please select units"

class VolumeScreen(Screen):
    def back_to_measurement(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'measurement_screen'
    def return_to_home(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home_screen'
    
    def calculate(self,v1,v2,input):
        if v1 != "Volume 1" and v2 != "Volume 2":
            if is_number(input):
                result = conversion.get_volume_conversion(v1,v2,input)
                display = "{0} {1} is {2} {3}.".format(input,v1,str(result),v2)
                self.ids.answer.text = display
            else:
                self.ids.answer.text = "Error, please check input."
        else:
            self.ids.answer.text = "Please select units"






###########################################

class AboutUs(Screen):
    def go_to_instagram(self):
        webbrowser.open("https://www.instagram.com/moneyhack.co/")
    
    def go_to_website(self):
        webbrowser.open("https://moneyhackco.wordpress.com")

    def back_to_home(self):
        self.manager.transition.direction = "right"
        self.manager.current = "home_screen"

class UserGuide(Screen):
    def back_to_home(self):
        self.manager.transition.direction = "right"
        self.manager.current = "home_screen"
    






###########################################

class MainApp(App):
    def build(self):
        self.icon = "CalculatorIcon.png"
        return RootWidget()




if __name__ == "__main__":
    MainApp().run()
