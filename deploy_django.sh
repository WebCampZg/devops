#!/bin/bash

cd ansible

ansible-playbook site.yml --tags=django --skip-tags=vagrant

