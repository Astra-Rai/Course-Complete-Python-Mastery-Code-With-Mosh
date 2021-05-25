# Installing a code runner


# To run open terminal window, and run ptyhon
# Go to extensions panel, search for: code runner
# Select Code Runner by Jun Han, .run, orange icon
# Install .run and then reload VSCode
# Now instead of openinging the terminal and typing python version and file name...
# ... press CTRL +   ALT +   n

print("Yo, Fam.What's good?") # test code runner, output worker

# change command that runs python from python -u to python3 if you're on a mac, right now it's python -u
# go to Code -> Preferences -> Settings -> right margin ... 
# in search bar type: code-runner.execu.....
# In the 'Default User Settings Window' this will lightly highlight: "code-runner.executorMap" : {
# scroll down and view command that is used to execute ptyhon code, right now mines is: "python": python -u
# this needs to be changed, we cannot change the default settings
# change the user settings, scroll down, afer the last setting..
# type a comman and in quotes type: "code-runner.executorMap" and press enter, copies settings in left side to right
# change python -u command to python3

