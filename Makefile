.PHONY: all deploy deploy-django deploy-web

all: deploy

deploy:
	cd ansible && ansible-playbook site.yml --skip-tags=vagrant

deploy-web:
	cd ansible && ansible-playbook site.yml --tags=web --skip-tags=vagrant

deploy-django:
	cd ansible && ansible-playbook site.yml --tags=django --skip-tags=vagrant

