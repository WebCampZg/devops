#!/bin/bash

cd ansible

ansible-playbook site.yml --skip-tags=vagrant

