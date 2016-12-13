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

ElasticSearch on YARN via Slider For HDP
========

ElasticSearch on YARN - Slider package for deploying ElasticSearch on YARN cluster.

Getting Started
========

Throughout these instructions, `$PROJECT_HOME` refers to the directory where you cloned this project.

**1) Download a ElasticSearch distribution archive (tar.gz)**

Download the latest ElasticSearch distribution from: https://www.elastic.co/downloads/elasticsearch

Once downloaded, move the distribution archive to `$PROJECT_HOME/package/files/elasticsearch-{version}.tar.gz`

The distribution archive must be named `elasticsearch-{version}.tar.gz` as the `metainfo.xml` file references this path.

**2) Create the elasticsearch-on-yarn.zip deployment package**

Create the Slider package using zip:

```
zip -r elasticsearch-on-yarn.zip metainfo.xml configuration/ package/ appConfig-default.json resources-default.json
```

**3) Copy the package to /var/lib/ambari-server/resources/apps/**

```
cp elasticsearch-on-yarn.zip /var/lib/ambari-server/resources/apps/
```

**4) Restart the Ambari server**

Restart your Ambari server:

```
ambari-server restart
```

Review the other settings in this file to verify they are correct for your environment.

**5) View application in Slider View ambari**

Then log into the Slider View, and the application will be available for users to deploy

**6) Deploy ElasticSearch on YARN**

Select the Create App button.

Choose the elasticsearch-on-yarn to deploy from the Applications Types drop-down menu, and then
provide a name for this instance

Additional configuration options will be loaded based on the JSON configuration files provided
with the application

Verify all settings and click Finish to launch the application

Then return to the Slider View home page and the newly launched application instance will be
listed.
