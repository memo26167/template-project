# Everything, but it does not reset environment
tox -c tox.ini --root components/component1/
tox -c tox.ini --root components/component2/

# Environment resetting
# tox -r -c tox.ini --root components/component1/

# Just selecting one environment
# tox -c tox.ini -e ruff --root components/component2/

# Just running pytest environment
# tox -c tox.ini -e py310 --root components/component3/

# Selecting just the fastest tests
# tox -c tox.ini --root components/component/ -- -m "not slow"