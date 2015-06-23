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
from yaml_config import yaml_config
import time
import os
import sys

def start_process(
    http_port,
    tcp_port,
    node_master,
    node_data):

    import params

    Directory([params.conf_dir],
            owner=params.es_user,
            group=params.user_group,
            recursive=True
    )

    yaml_config( "elasticsearch.yml",
               conf_dir = params.conf_dir,
               configurations = params.config['configurations']['elasticsearch'],
               owner = params.es_user,
               group = params.user_group
    )
    
    start_es_cmd = """{java64_home}/bin/java
{es_child_opts}
-Des.http.port={http_port}
-Des.transport.tcp.port={tcp_port}
-Des.node.master={node_master}
-Des.node.data={node_data}
org.elasticsearch.bootstrap.Elasticsearch"""

    process_cmd = format(start_es_cmd.replace("\n", " "))
    print("Starting ElasticSearch using command: "+process_cmd)
    Execute(process_cmd,
        logoutput=True,
        wait_for_finish=False,
        pid_file=params.pid_file,
        poll_after = 10,
        cwd=format("{app_root}")
    )  


def stop_process(pid_file):
    process_dont_exist = format("! ({no_op_test})")
    pid = format("`cat {pid_file}` >/dev/null 2>&1")
    Execute(format("kill {pid}"),
            not_if=process_dont_exist
    )
    Execute(format("kill -9 {pid}"),
            not_if=format("sleep 2; {process_dont_exist} || sleep 20; {process_dont_exist}"),
            ignore_failures=True
    )
    Execute(format("rm -f {pid_file}"))

