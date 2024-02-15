import locale

# Use a loop to see languages in the module.
# We can't use locale_alias by itself because it's in the
# locale namespace (a collection of code that exists in
# a different space).
for l in locale.locale_alias:
    print(l)