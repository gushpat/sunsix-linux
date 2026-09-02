
Sunsix Linux — Análise Técnica e Estado da Pesquisa
Documento consolidado para o projeto de preservação digital
1. Objetivo e escopo
Este documento consolida, em um único registro, o conhecimento técnico e histórico reunido até o momento
sobre o Sunsix Linux. O objetivo é documentar a mídia preservada, identificar sua base de software,
compreender sua arquitetura e localizar as possíveis camadas de customização OEM, sem alterar ou
reconstruir o sistema. Evidências observadas diretamente na ISO devem ser distinguidas de conclusões
obtidas por comparação histórica.
O projeto associado ao estudo é um projeto de preservação digital, e não uma tentativa de criar uma nova
distribuição Linux.
2. Projeto de preservação
O repositório público gushpat/sunsix-linux registra o Sunsix Linux como uma distribuição GNU/Linux brasileira
associada a computadores OEM Sunsix comercializados no Brasil na segunda metade dos anos 2000. O
repositório organiza a pesquisa em história, hardware, preservação, análise técnica e troubleshooting.
Repositório: https://github.com/gushpat/sunsix-linux
3. Identificação consolidada do sistema
Item Informação atual
Nome Sunsix Linux
Origem Brasil
Período estimado 2007–2008
Mídia CD-ROM
Base Ubuntu 7.04 Feisty Fawn
Arquitetura i386 / x86 32-bit
Desktop GNOME 2.18
Kernel Linux 2.6.20; evidências do ambiente indicam série 2.6.20-15
Pacotes APT / dpkg
Live system Arquitetura Ubuntu baseada em casper
Instalação Ubiquity / instalador gráfico do Ubuntu
Estado Preservado e em investigação
4. Integridade da mídia preservada
Checksum SHA-256 registrado para a ISO preservada:
859a058aaffb378d7a01c6420ac81a9d81f983967e4b880a7c3eb1301280b388.
O checksum deve ser tratado como identificador da cópia atualmente preservada. Uma mídia diferente com
checksum diferente não deve ser descartada: pode representar outra revisão, imagem ou lote de distribuição.
5. Evidências sobre a base Ubuntu
A identificação como Ubuntu 7.04 Feisty Fawn é coerente com a estrutura e os componentes observados na
mídia analisada: casper, Ubiquity, APT/dpkg, kernel da série 2.6.20, ambiente GNOME da geração 2.18 e
conjunto de pacotes característico do Feisty.
Documentação histórica do próprio Ubuntu confirma que o Feisty utilizava Linux 2.6.20, GNOME 2.18,
OpenOffice.org 2.2 e X.Org 7.2. A documentação histórica também identifica o Desktop CD i386 como a
mídia destinada aos PCs x86 comuns.
6. O que a análise do manifesto de pacotes já indica
O inventário de pacotes analisado anteriormente apresenta um sistema fortemente baseado no Ubuntu
Feisty, sem uma quantidade evidente de pacotes cujo nome contenha 'sunsix'. Isso é importante: a ausência
de nomes de pacotes com a marca não significa ausência de customização OEM.
Foram observados componentes e versões compatíveis com a época, incluindo Firefox 2.0.0.x,
OpenOffice.org da geração 2.2, componentes de Flash da época, pacotes de idioma e atualizações do Feisty.
Alguns pacotes como smartdimmer e toshset aparecem no inventário, mas não devem ser classificados como
software Sunsix sem comparação com uma instalação Ubuntu Feisty original.
A hipótese atual mais forte é que a customização Sunsix tenha sido majoritariamente realizada por
configuração, artwork, seleção de pacotes, arquivos de inicialização e ajustes do ambiente, em vez de uma
grande coleção de pacotes próprios.
7. Por que a busca por 'sunsix' nos nomes não foi
suficiente
A busca realizada com unsquashfs -l filesystem.squashfs | grep -i sunsix não encontrou
resultados. Isso não constitui evidência de que o sistema não possua customizações Sunsix. OEMs podem
substituir arquivos existentes, alterar configurações, instalar artwork em diretórios genéricos, modificar
defaults do GNOME, alterar o GDM, o usplash ou o instalador, e até incorporar mudanças dentro de scripts
sem inserir a marca no nome do arquivo.
8. Camadas onde a customização deve ser procurada
Camada Locais/elementos relevantes
ISO/boot isolinux/, arquivos de configuração, menu de boot, parâmetros, splash, volume ID, El Torito
Live system casper/, filesystem.squashfs, initrd
Identidade /etc/lsb-release, /etc/issue, /etc/issue.net, metadados e arquivos de identificação
APT /etc/apt/sources.list, listas de pacotes, versões e repositórios
Pacotes /var/lib/dpkg/status, /var/lib/dpkg/info/, .deb em pool/
GNOME /etc/gconf/, defaults do desktop, menus e configurações
GDM /etc/gdm/ e telas/configurações de login
X.Org /etc/X11/ e arquivos de configuração de vídeo
Artwork /usr/share/backgrounds/, pixmaps/, icons/, themes/, gnome-background-properties/
Boot splash /usr/lib/usplash/, /etc/usplash.conf e componentes relacionados
Ubiquity /usr/share/ubiquity/ e arquivos de interface/branding
Scripts/OEM /opt/, /usr/local/, /etc/init.d/, scripts e executáveis incomuns
Perfil padrão /etc/skel/, defaults do usuário, configurações GNOME
9. Estrutura esperada da ISO
A mídia deve ser tratada como uma cadeia de componentes: mídia ISO/El Torito → carregador de boot →
kernel/initrd → casper → filesystem.squashfs → sistema de arquivos do ambiente live → Ubiquity →
instalação no disco. Além disso, a própria ISO pode conter um repositório APT parcial em dists/ e pool/.
O estudo deve registrar quais desses componentes são idênticos ou próximos ao Ubuntu Feisty original e
quais apresentam alterações específicas do OEM.
10. Modelo técnico do sistema
Em termos arquiteturais, o Sunsix Linux deve ser entendido como uma distribuição OEM derivada de uma
base Ubuntu, e não como um sistema operacional construído integralmente do zero. A camada inferior é o
kernel Linux; acima dela ficam os componentes GNU/Linux e a infraestrutura Debian/Ubuntu de pacotes; a
sessão gráfica é baseada no GNOME 2.18; o meio live utiliza casper; e a instalação em disco é feita pelo
Ubiquity.
Essa arquitetura explica por que uma análise de customização precisa olhar além dos nomes de arquivos: a
maior parte da identidade do produto pode estar em configurações e arquivos substituídos dentro de
componentes que continuam com nomes Ubuntu.
11. Evidências históricas externas
Há evidências históricas independentes de que computadores Sunsix eram comercializados no Brasil com
Linux pré-instalado. Registros e anúncios de época associam máquinas Sunsix a processadores Intel e AMD,
memória DDR2, discos SATA e software Linux. Discussões de usuários também associam explicitamente o
'Linux Sunsix' a computadores da marca.
Uma evidência particularmente relevante é o registro histórico de uma máquina Sunsix que teria vindo com
Ubuntu Linux, além de relatos que identificam Ubuntu 7.04 Feisty em computadores Sunsix. Isso reforça a
hipótese de que a mídia preservada seja uma customização OEM do Ubuntu.
O Ubuntu 7.04 foi lançado em abril de 2007 e o suporte da versão terminou posteriormente; portanto, a
presença de pacotes atualizados da série Feisty pode indicar uma imagem produzida algum tempo após o
lançamento inicial.
12. Estado atual da investigação
Item Estado
ISO original Preservada
Checksum Confirmado
Arquitetura Identificada como i386
Base Identificada como Ubuntu 7.04 Feisty
Desktop Identificado como GNOME 2.18
Kernel Identificado como 2.6.20 / série 2.6.20-15
Sistema de pacotes APT/dpkg
Execução virtual Testável
Lista de pacotes Em análise
Customizações OEM Em investigação
Hardware original Em investigação
Documentação original Procurando
CD de drivers/extras Procurando
Data exata da ISO Não determinada
Autor/desenvolvedor da customização Não determinado
13. Perguntas de pesquisa ainda abertas
• Qual a data exata de criação da ISO?
• A imagem preservada corresponde ao primeiro release Sunsix ou a uma revisão posterior?
• Quem produziu a customização OEM?
• Quais arquivos foram modificados em relação ao Ubuntu 7.04 original?
• Existem pacotes próprios da Sunsix com nomes neutros?
• Existem scripts ou binários exclusivos?
• Quais modelos de computadores Sunsix receberam essa mídia?
• Existia mais de uma ISO?
• O CD azul correspondia ao sistema e havia um CD laranja separado para drivers/extras?
• Existem manuais, notas de instalação, adesivos, fotografias ou documentos originais?
• Qual era o processo de distribuição da mídia junto aos computadores?
• Quais temas, wallpapers, ícones, sons e configurações eram exclusivos?
14. Metodologia recomendada para a análise
1. Preservar a ISO original e registrar seu checksum antes de qualquer manipulação.
2. Trabalhar sempre sobre cópias extraídas, mantendo a mídia original intacta.
3. Inventariar a estrutura da ISO antes de extrair ou modificar conteúdo.
4. Catalogar casper, kernel, initrd, bootloader e arquivos de configuração.
5. Extrair o filesystem.squashfs para uma árvore de análise.
6. Registrar versões e nomes de todos os pacotes instalados.
7. Comparar o manifesto com uma imagem Ubuntu 7.04 i386 de referência.
8. Pesquisar diferenças em /etc, /usr/share, /opt, /usr/local, GConf, GDM, X.Org e usplash.
9. Examinar scripts de instalação e pós-instalação dos pacotes suspeitos.
10. Separar cada descoberta em: evidência direta, evidência indireta ou hipótese.
11. Registrar hashes e caminhos dos arquivos relevantes para permitir reprodução da pesquisa.
15. Segurança e preservação
O sistema é extremamente antigo e não deve ser utilizado como sistema operacional principal ou conectado
diretamente à Internet. A experimentação deve ocorrer preferencialmente em máquina virtual, com rede
desativada ou isolada e snapshots. O objetivo desta pesquisa é histórico e técnico.
16. Fontes e referências principais
• Repositório de preservação: https://github.com/gushpat/sunsix-linux
• Ubuntu 7.04 — arquivo histórico de releases: https://old-releases.ubuntu.com/releases/7.04/
• Ubuntu 7.04 Beta / informações técnicas históricas: https://ubuntu.com/blog/ubuntu-7-04-beta
• Artigos históricos de instalação e uso do Ubuntu 7.04 em comuni
