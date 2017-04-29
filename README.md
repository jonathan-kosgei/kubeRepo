docker run --rm -v ${PWD}:/local \
swaggerapi/swagger-codegen-cli generate \
-i /local/swagger.yml \
-l python \
-c /local/python.json \
-o /local/out \
--git-repo-id kubeRepo \
--git-user-id jonathan-kosgei