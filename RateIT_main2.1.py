
##      RateIT 2.0 by Brian Preece

##      A SIMPLE PROGRAM THAT COLLECTS USER INPUT, AND THEN
##      ASKS THE USER TO RATE CHARACTERISTICS OF THE INPUT.
##      RETURNS THE AVERAGE RATINGS OF EACH CHARACTERISTIC OVER
##      MULTIPLE ITERATIONS.



class View:
    ''' responsible for the output and display of user provided data '''

    #def __init__(self, links):
    #    links = self.links


    def show_cat(self):                                       
    # creates a list of user-created categories
        self.index = 0
        for i in categories:
            self.index += 1
            print (self.index, '=', i)
        print ()



    def pick_cat(self):                                       
        print ('what category would you like to view?')
        self.user_select = (int(input('option: ')) - 1)
        if self.user_select in range (0, len(categories)):
            self.user_dict = json.load(open('rateIT_' + categories[self.user_select] + '.txt', 'r'))
            v.display_dic(self.user_dict, self.user_select)
        else:
            print ('oops! that didnt work... \nplease try again.\n')
            v.show_cat()

    

    def display_dic(self, user_dict, user_select):
        '''display the rankings from a dictionary'''
        name = categories[user_select]
        print ('how would you like to view', name,'?\n1 = by element \n2 = by characteristic\n')
        self.user_select = int(input('option: '))
        if self.user_select == 1:
            print ('what element would you like to view?') 
            index = 1
            for i in user_dict.keys():
                if i != name:
                    print (index, '=', i)
                    index += 1
            user_input = int(input('==> '))
            if user_input in range(0, len(user_dict.keys())):
                print ('I FOUND IT!????')

        elif self.user_select == 2:
            v.display_by_characteristic(user_dict, name)
            
        
    def display_by_element(self, user_dict, element):
        print ('i need to add more code here................')



    def display_by_characteristic(self, user_dict, name):
        index = 1
        for i in user_dict[name]:
            print (index,'=',i)
            index += 1
        user_input = int(input('plesae pick a characteristic to display: '))
        print ('i need to add more code here..................')
        




class Create:
    ''' responsible for creating libraries for user to rate '''

    #def __init__(self, name):
    #    self.name = name
    
    def user_add(self):
        '''
        asks user to add an item to be ranked.
        '''
        print ('Great! So far you have added these categories:\n')
        v.show_cat() #prints a list of categories
        self.user_input = input('Please pick an option above, or enter a new category: ').lower()

        if self.user_input not in categories:
            categories.append(self.user_input)
            links.append('rateIT_' + self.user_input + '.txt')  
            json.dump(links, open('rateIT_index.txt', 'w'))
            print ('\nI have added', self.user_input, 'to your database!')
            self.user_create_char(self.user_input)
        else:
            print ('that was already added!')
        welcome_screen()



    def user_create_char(self, user_input):
        '''
        asks the user to add the characteristics to be rated of a certain category
        '''
        self.characteristics = []
        self.char = ''
        print ('please add the characteristics of', user_input, 'you would like to rate\n'
               "type 'q' when you are finished.\n")
        num = 0
        while self.char != 'q':
            num += 1
            self.char = input('characteristic: ')
            if self.char != 'q':
                self.characteristics.append(self.char)
        c.create_dictionary(user_input, self.characteristics)
        
        print ('\ngreat! you can rate each of those characteristics now!')
        
        welcome_screen()

    def create_dictionary(self, name, characteristics):
        user_dict = {}
        user_dict[name] = characteristics
        json.dump(user_dict, open('rateIT_' + name + '.txt', 'w'))




class Rate:
    ''' Responisble for collection of user input'''
    
    #def __init__(self, name):
    #   self.name = name
    
    def user_select_rate(self):
        '''
        asks user what item they want to rate
        '''
        print ('lets rate something!\n'
               'what category would you like to view?\n')
        i = 0
        # print out all items in category list
        for each in categories:
            i += 1
            print (i,'=',each)
        self.user_input = int(input('\noption: '))

        if self.user_input in range(0, len(categories)+1):
            self.selected = categories[self.user_input-1]
            #print ('you have selected', self.selected)
            r.user_rate(self.selected)
        else:
            print ('--------------------------\n'
                   'oops! lets try that again\n')
            self.user_input = 0
            r.user_select_rate()



    def collect_items(self, user_dic, name):
        
        print ('you have selected', name, 'which has the characteristics: ', user_dic[name])
        print ('please select an items number to rate, or add a new item by typing it in...')
        print ()
        start = 0
        for key in user_dic:
            if key != name:
                start += 1
                print (start, '=', key) 



    def user_rate(self, name):
        '''
        asks the user to rank each characterisitc of an item from 0-10.
        '''
        self.ratings = []
        
        self.user_dic = json.load(open('rateIT_' + name + '.txt', 'r'))
        r.collect_items(self.user_dic, name)
        self.user_input = input('==> ')
        
        print ('Great! please rank each characteristic of ', self.user_input, ' from 0-10\n')

        ranked = 1
        for i in self.user_dic[name]:
            self.user_select = int(input(i + '= '))
            self.ratings.append(self.user_select)
        self.new_ratings = [self.ratings, ranked]
        r.update_rate(self.new_ratings, self.user_dic, name, self.user_input)


    def update_rate(self, new_ratings, user_dic, category, element):
        '''
        updates the dictionary of total rankings
        '''    
        if element not in user_dic:
            user_dic[element] = new_ratings
            json.dump(user_dic, open('rateIT_' + category + '.txt', 'w'))

        elif element in user_dic:
            times_ranked = user_dic[element][1] + new_ratings[1]
            total_ranked = [x + y for x, y in zip(user_dic[element][0], new_ratings[0])]
            user_dic[element] = [total_ranked, times_ranked]
            json.dump(user_dic, open('rateIT_' + category + '.txt', 'w'))




def welcome_screen():
    ''' asks user to CREATE, RATE, VIEW or QUIT'''
    global start
    if start == 0:
        print('\nWelcome to RateIT 2.0.... \n'
              '....a journal of thoughts\n')
        start += 1    
    if len(categories) > 0:
        print ('please pick an option....\n\n'
           '1 = CREATE\n2 = RATE\n3 = VIEW\n4 = QUIT\n')
    else:
        print ('please pick an option....\n\n'
           '1 = CREATE\n4 = QUIT\n')

    user_input = int(input('option: '))

    if user_input==1:
        c.user_add()
    elif user_input == 2:
        r.user_select_rate()
    elif user_input == 3:
        v.show_cat()
        v.pick_cat()
    elif user_input == 4:
        print ('\nGoodbye!\n')
        start = 1
    else:
        print ('\noops! lets try that again\n')
        welcome_screen()   
            
    

    
import json
file = 'rateIT_index.txt'
open_file = json.load(open(file, 'r+'))
#read_file = open_file.readlines()

links = [] # list of rateIT files previously created
for i in open_file:
    links.append(i)

categories = [] # list of categories previously created
for i in links:  
    i = i.lstrip('rateIT_')
    i = i[:-4] # this removes the extention '.txt'
               # using i.rstrip('.txt') removed the 't' from 'fruit'...'frui'
    categories.append(i)



start = 0

v = View()
c = Create()
r = Rate()

welcome_screen() # initalize program
