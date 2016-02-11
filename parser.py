# Plotkin, Benjamin
# 31st January, 2016

# using Python's regular expressions library
import re

# my RE patterns could be further refined, this is a simple exercise

### decimal RE pattern ###
# can either be a single zero, or any integer with a non-zero leading digit; no
# other characters are allowed except leading negative sign. ###
chkDec = re.compile(r"(^0$)|(^\-?[1-9]+[0-9]*$)");

### floating point RE pattern ###
# must have a non-zero leading digit, followed by a decimal point, with one or
# more digits following; no other chars allowed except leading neg sign. ###
chkFlt = re.compile(r"^\-?[1-9]+[0-9]*\.[0-9]+$");

### octal RE pattern ###
# can either be two or more zeros, or MUST have leading zero, followed by one or
# more digits from zero to seven; no other chars allowed except leading negative
# sign on non-zero number; NOTE: Single zero is ALWAYS determined a decimal. ###
chkOct = re.compile(r"0(0+)$|^\-?0+[0-7]+$");

### scientific notation RE pattern ###
# can have a leading negative symbol; must have single non-zero leading digit;
# optionally can have one decimal point with one or more digits following; MUST
# be followed by "e" or "E", optionally followed by single negative symbol; MUST
# end with one or more digits. ###
chkScN = re.compile(r"^\-?[1-9](\.[0-9]+)?[e|E]\-?[0-9]+$");

# using infinite loop as per spec (loop exits via python interpreter exit)
while True:
  # prompt user for string input
  myStr = raw_input("Enter a value: ");

  # match user-provided string with each RE pattern and trap for a match;
  # precedence is not important because RE patterns are mutually exclusive. ###
  isDec = chkDec.match(myStr);
  isFlt = chkFlt.match(myStr);
  isOct = chkOct.match(myStr);
  isScN = chkScN.match(myStr);

  # error case is the fall-through default
  if isDec:
    print ("      '" + myStr + "' is a decimal number.");
  elif isFlt:
    print ("      '" + myStr + "' is a floating point number.");
  elif isOct:
    print ("      '" + myStr + "' is an octal number.");
  elif isScN:
    print ("      '" + myStr + "' is a scientific notation number.");
  else:
    print ("      '" + myStr + "' is an error.");
# end while
