str=input("Enter your sentence:")
consonant=0
vowel=0
for ch in str:
   if ch.isalpha():
       if ch.lower() in "aeiou":
      	 vowel+=1
       else:
      		  consonant+=1
   print("vowel=",vowel)
   print("consonant=",consonant)
   
