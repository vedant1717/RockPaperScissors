rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random as rd
print('''                                       ,   ,
                                        $,  $,     ,
                                        "ss.$ss. .s'
                                ,     .ss$$$$$$$$$$s,
                                $. s$$$$$$$$$$$$$$`$$Ss
                                "$$$$$$$$$$$$$$$$$$o$$$       ,
                               s$$$$$$$$$$$$$$$$$$$$$$$$s,  ,s
                              s$$$$$$$$$"$$$$$$""""$$$$$$"$$$$$,
                              s$$$$$$$$$$s""$$$$ssssss"$$$$$$$$"
                             s$$$$$$$$$$'         `"""ss"$"$s""
                             s$$$$$$$$$$,              `"""""$  .s$$s
                             s$$$$$$$$$$$$s,...               `s$$'  `
                         `ssss$$$$$$$$$$$$$$$$$$$$####s.     .$$"$.   , s-
                           `""""$$$$$$$$$$$$$$$$$$$$#####$$$$$$"     $.$'
                                 "$$$$$$$$$$$$$$$$$$$$$####s""     .$$$|
                                  "$$$$$$$$$$$$$$$$$$$$$$$$##s    .$$" $
                                   $$""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"   `
                                  $$"  "$"$$$$$$$$$$$$$$$$$$$$S""""'
                             ,   ,"     '  $$$$$$$$$$$$$$$$####s
                             $.          .s$$$$$$$$$$$$$$$$$####"
                 ,           "$s.   ..ssS$$$$$$$$$$$$$$$$$$$####"
                 $           .$$$S$$$$$$$$$$$$$$$$$$$$$$$$#####"
                 Ss     ..sS$$$$$$$$$$$$$$$$$$$$$$$$$$$######""
                  "$$sS$$$$$$$$$$$$$$$$$$$$$$$$$$$########"
           ,      s$$$$$$$$$$$$$$$$$$$$$$$$#########""'
           $    s$$$$$$$$$$$$$$$$$$$$$#######""'      s'         ,
           $$..$$$$$$$$$$$$$$$$$$######"'       ....,$$....    ,$
            "$$$$$$$$$$$$$$$######"' ,     .sS$$$$$$$$$$$$$$$$s$$
              $$$$$$$$$$$$#####"     $, .s$$$$$$$$$$$$$$$$$$$$$$$$s.
   )          $$$$$$$$$$$#####'      `$$$$$$$$$###########$$$$$$$$$$$.
  ((          $$$$$$$$$$$#####       $$$$$$$$###"       "####$$$$$$$$$$
  ) \         $$$$$$$$$$$$####.     $$$$$$###"             "###$$$$$$$$$   s'
 (   )        $$$$$$$$$$$$$####.   $$$$$###"                ####$$$$$$$$s$$'
 )  ( (       $$"$$$$$$$$$$$#####.$$$$$###' -Tua Xiong     .###$$$$$$$$$$"
 (  )  )   _,$"   $$$$$$$$$$$$######.$$##'                .###$$$$$$$$$$
 ) (  ( \.         "$$$$$$$$$$$$$#######,,,.          ..####$$$$$$$$$$$"
(   )$ )  )        ,$$$$$$$$$$$$$$$$$$####################$$$$$$$$$$$"
(   ($$  ( \     _sS"  `"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$S$$,
 )  )$$$s ) )  .      .   `$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"'  `$$
  (   $$$Ss/  .$,    .$,,s$$$$$$##S$$$$$$$$$$$$$$$$$$$$$$$$S""        '
    \)_$$$$$$$$$$$$$$$$$$$$$$$##"  $$        `$$.        `$$.
        `"S$$$$$$$$$$$$$$$$$#"      $          `$          `$
            `"""""""""""""'         '           '         ''')
usr_choice=int(input("Enter your selection amonsgt rock, paper and scissors as 0,1,2 respectively:\n"))
computer_choice = rd.randint(0,2)
print(f"Computer choose {computer_choice}")
if usr_choice == 0 and computer_choice == 2:
  print(f"Your choose Rock \n{rock}")
  print(f"Computer chose Scissors \n{scissors}")
  print("You Won!")
elif usr_choice == 0 and computer_choice ==1:
  print(f"You choose Rock\n{rock}")
  print(f"Computer choose Paper\n{paper}")
  print("Computer Won!")
elif usr_choice == 0 and computer_choice ==0:
  print(f"You choose Rock\n{rock}")
  print(f"Computer choose Rock\n{rock}")
  print("It's a tie!")
elif usr_choice == 1 and computer_choice ==0:
  print(f"You choose Paper\n{paper}")
  print(f"Computer choose Rock\n{rock}")
  print("You Won!")
elif usr_choice == 1 and computer_choice ==1:
  print(f"You choose Paper\n{paper}")
  print(f"Computer choose Paper\n{paper}")
  print("It's a tie!")
elif usr_choice == 1 and computer_choice ==2:
  print(f"You choose Paper\n{paper}")
  print(f"Computer choose Scissors\n{scissors}")
  print("Computer Won!")
elif usr_choice == 2 and computer_choice ==0:
  print(f"You choose Scissors\n{scissors}")
  print(f"Computer choose Rock\n{rock}")
  print("Computer Won!")
elif usr_choice == 2 and computer_choice ==1:
  print(f"You choose Scissors\n{scissors}")
  print(f"Computer choose Paper\n{paper}")
  print("You Won!")
elif usr_choice == 2 and computer_choice ==2:
  print(f"You choose Scissors\n{scissors}")
  print(f"Computer choose Scissors\n{scissors}")
  print("It's a tie!")
else:
  print("You chose an invalid number!")

