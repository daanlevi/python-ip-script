### install and run Jenkins job

The multi pipeline job can be installed using the Jenkins api.

`curl -s -X POST 'https://username:token@jenkins.host.name/createItem?name=projectname' --data-binary @multibranch.xml -H "Content-Type:text/xml"`
