RESOURCE = resource.txt
SAMPLE = sample_resource.txt

.phony: part-one-sample, part-two-sample, part-one, part-two, run, help

run: part-one part-two

part-one-sample:
	python part_one.py $(SAMPLE)

part-one:
	python part_one.py $(RESOURCE)

part-two-sample:
	@python part_two.py $(SAMPLE)

part-two:
	@python part_two.py $(RESOURCE)

help:
	@echo "Targets are:"
	@echo "- part-one-sample"
	@echo "- part-one"
	@echo "- part-two-sample"
	@echo "- part-two"
