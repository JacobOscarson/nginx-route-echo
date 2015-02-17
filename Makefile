# If you are on OS X, you might need to run it like:
#   $ CC=clang make

bin/pip:
	@echo 'need pip'
	curl https://raw.githubusercontent.com/pypa/virtualenv/master/virtualenv.py \
		> virtualenv.py
	# - to ignore error, tend to throw with a 'No module named pip'
	-python2.7 virtualenv.py .
	curl https://bootstrap.pypa.io/get-pip.py > get-pip.py
	./bin/python get-pip.py
	./bin/pip install fabric
	rm -rf ./get-pip.py ./virtualenv.py

.PHONY: clean
clean:
	rm -rf bin/ include/ lib/ virtualenv.py get-pip.py pip-selfcheck.json
