# If installed as: pdm sync --dev --no-editable
from my_package import MY_VARIABLE
print(MY_VARIABLE)

# If installed as: pdm sync --dev
from my_package.my_package import MY_VARIABLE
print(MY_VARIABLE)
