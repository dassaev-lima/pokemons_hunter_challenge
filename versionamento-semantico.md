### As bibliotecas selecionadas para a análise de versionamento semântivo foram a Pylint e Pycycle

Ambas as biblioteca possuem uma estrutura de versionamento semântico nos níveis

- MAJOR: Aumenta quando há mudanças incompatíveis com versões anteriores.
- MINOR: Aumenta quando há adição de novas funcionalidades que são compatíveis com versões anteriores.
- PATCH: Aumenta para correções de bugs e melhorias menores que são compatíveis com a versão anterior.

atualmente sendo usada no projeto com as respectivas versões

- Pylint==3.2.6
- Pycycle==0.0.8

Em relação ao versionamento LTS nenhuma das duas bibliotecas tem esse tipo de suporte, possuem atualização com frequência, e podem receber correções de bugs e adicionais de funcionalidades, no entando não ha uma garantia por um tempo específico.

Não foi encontrado em nenhuma das libs uma especificação de tempo de suporte para as versões. Mas alguns links podem ajudar no futuro

https://github.com/pylint-dev/pylint/milestones

https://pypi.org/project/pycycle/#history

### Para análise Semântica e LTS

O python foi escolhido para exemplificar o uso de uma ferramenta com versionamento semãntito com os 3 níves 

- MAJOR: Aumenta quando há mudanças incompatíveis com versões anteriores.
- MINOR: Aumenta quando há adição de novas funcionalidades que são compatíveis com versões anteriores.
- PATCH: Aumenta para correções de bugs e melhorias menores que são compatíveis com a versão anterior.

e também possui suporte LTS bem definido, 5 anos após o lançamento. Mais detalhes sobre o suporte estão presentes no link abaixo:

https://peps.python.org/pep-0602/
