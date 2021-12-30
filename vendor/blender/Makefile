AUTO_YAML:=$(patsubst %.yaml.json,%.yaml,$(wildcard *.yaml.json))

all: $(AUTO_YAML)


%.yaml: %.yaml.json %.yaml.head
	cat $(word 2,$^) > $@
	../../_tools/make_fmtstr_check.py $(word 1,$^) >> $@
