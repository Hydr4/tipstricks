# Tips&Tricks no.1

name = 'Abdelrahman'
age = 20

print 'My name is '+name+', I am '+str(age)+' years old.'              # DO NOT do this.
print ' '.join(['My name is', name, ', I am', str(age), 'years old.']) # DO THIS, why?
                                                                       # Fast and common to use.
print 'My name is %s, I am %s years old.' %(name, age)                 # Do this also.