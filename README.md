<!---
   Licensed to the Apache Software Foundation (ASF) under one or more
   contributor license agreements.  See the NOTICE file distributed with
   this work for additional information regarding copyright ownership.
   The ASF licenses this file to You under the Apache License, Version 2.0
   (the "License"); you may not use this file except in compliance with
   the License.  You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
-->

ElasticSearch on YARN via Slider
========

ElasticSearch on YARN - Slider package for deploying ElasticSearch on YARN cluster.

Getting Started
========

Follow the instructions for getting started with Slider:
http://slider.incubator.apache.org/docs/getting_started.html

Be sure to add the `$SLIDER_HOME/bin` directory to your path.

Also, make sure your `conf/slider-client.xml` file sets the ResourceManager address so you don't have to
include the `--manager` parameter with every slider command.

```
  <property>
    <name>yarn.resourcemanager.address</name>
    <value>localhost:8032</value>
  </property>
```

Throughout these instructions, `$PROJECT_HOME` refers to the directory where you cloned this project.

**1) Download a ElasticSearch distribution archive (tar.gz)**

Download the latest ElasticSearch distribution from: https://www.elastic.co/downloads/elasticsearch

Once downloaded, move the distribution archive to `$PROJECT_HOME/package/files/elasticsearch.tar.gz`

The distribution archive must be named `elasticsearch.tar.gz` as the `metainfo.xml` file references this path.

**2) Create the elasticsearch-on-yarn.zip deployment package**

Create the Slider package using zip:

```
zip -r elasticsearch-on-yarn.zip metainfo.xml configuration/ package/
```

**3) Install the package on HDFS**

```
slider package --install --replacepkg --name ES --package $PROJECT_HOME/elasticsearch-on-yarn.zip
```

**4) Configure environment specific settings**

Edit the `$PROJECT_HOME/appConfig-default.json`. At a minimum, you'll need to update the following settings
to match your environment:

```
    "java_home": "/usr/jdk64/jdk1.7.0_67",
    "site.global.app_root": "${AGENT_WORK_ROOT}/app/install/elasticsearch-1.6.0",
```

Review the other settings in this file to verify they are correct for your environment.

**5) Configure the number of ElasticSearch nodes to deploy**

Edit `yarn.component.instances` in `resources-default.json` to set the number of ElasticSearch nodes to deploy across your cluster.

**6) Deploy ElasticSearch on YARN**

```
slider create ES --template $PROJECT_HOME/appConfig-default.json \
  --resources $PROJECT_HOME/resources-default.json
```
