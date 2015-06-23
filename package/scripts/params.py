#!/usr/bin/env python
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

from resource_management import *

# server configurations
config = Script.get_config()

app_root = config['configurations']['global']['app_root']
java64_home = config['hostLevelParams']['java_home']
app_user = config['configurations']['global']['app_user']
conf_dir = format("{app_root}/config")
es_user = config['configurations']['global']['app_user']
user_group = config['configurations']['global']['user_group']
pid_file = config['configurations']['global']['pid_file']
master_http_port = config['configurations']['global']['master_http_port']
worker_http_port = config['configurations']['global']['worker_http_port']
master_tcp_port = config['configurations']['global']['master_tcp_port']
worker_tcp_port = config['configurations']['global']['worker_tcp_port']
es_master_host = config['configurations']['global']['es_master_host']
es_worker_host = config['configurations']['global']['es_worker_host']
es_child_opts = config['configurations']['global']['es_child_opts']