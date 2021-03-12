#
# Hypertag built-ins that are common to all target languages.
#
# They can be imported manually into a script with a statement of the form:
#
#    from hypertag.builtins import %dedent
#


from hypertag.std.builtins import register

__tags__ = register.tags

del globals()['register']
