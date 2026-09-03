# 🔬 Sunsix Linux — Dossiê Técnico de Preservação

> **Documento de investigação técnica da mídia preservada.**

Este documento registra o conhecimento técnico obtido durante a análise do **Sunsix Linux**, uma distribuição GNU/Linux brasileira associada a computadores OEM Sunsix comercializados no Brasil durante a segunda metade dos anos 2000.

O objetivo não é reconstruir ou modernizar o sistema, mas **preservar a mídia original, compreender sua arquitetura e identificar as modificações que transformaram uma base Ubuntu em um produto OEM da Sunsix**.

---

# 🧾 1. O Artefato Preservado

A investigação parte de uma imagem ISO original preservada.

| Propriedade       | Informação                   |
| ----------------- | ---------------------------- |
| Sistema           | Sunsix Linux                 |
| Tipo              | Distribuição OEM             |
| Origem            | Brasil                       |
| Mídia             | CD-ROM                       |
| Arquitetura       | i386 / x86 32-bit            |
| Base identificada | Ubuntu 7.04 Feisty Fawn      |
| Estado            | Preservado e em investigação |

## Integridade

O SHA-256 da cópia atualmente preservada é:

```text
859a058aaffb378d7a01c6420ac81a9d81f983967e4b880a7c3eb1301280b388
```

Esse checksum identifica especificamente a mídia analisada neste projeto.

> ⚠️ Uma mídia diferente não deve ser descartada apenas porque possui outro checksum. Diferenças podem indicar outra revisão, lote ou versão do sistema.

---

# 🔬 2. Resultado Atual da Investigação

## Identificação consolidada

| Componente                      | Identificação atual            | Confiança                    |
| ------------------------------- | ------------------------------ | ---------------------------- |
| Sistema                         | Sunsix Linux                   | 🟢 Confirmado                |
| Arquitetura                     | i386 / x86 32-bit              | 🟢 Confirmado                |
| Base                            | Ubuntu 7.04 Feisty Fawn        | 🟢 Confirmado                |
| Desktop                         | GNOME 2.18                     | 🟢 Confirmado                |
| Kernel                          | Linux 2.6.20 / série 2.6.20-15 | 🟢 Confirmado                |
| Pacotes                         | APT / dpkg                     | 🟢 Confirmado                |
| Live System                     | Casper                         | 🟢 Confirmado                |
| Instalador                      | Ubiquity                       | 🟢 Confirmado                |
| Customização OEM                | Presente                       | 🟡 Investigação em andamento |
| Principal forma de customização | Configuração e artwork         | 🟡 Hipótese forte            |
| Autor da customização           | Desconhecido                   | 🔴 Não identificado          |
| Data exata da ISO               | Desconhecida                   | 🔴 Não determinada           |

---

# 🟢 3. Como as Evidências São Classificadas

Para evitar que hipóteses sejam confundidas com fatos, esta investigação utiliza quatro níveis de confiança.

| Símbolo | Classificação    | Significado                                                               |
| ------- | ---------------- | ------------------------------------------------------------------------- |
| 🟢      | Confirmado       | Observado diretamente na mídia ou em evidência primária                   |
| 🟡      | Inferência forte | Sustentado por múltiplas evidências, mas ainda não diretamente confirmado |
| 🔵      | Relato histórico | Informação proveniente de terceiros ou documentação externa               |
| 🔴      | Desconhecido     | Ainda não existe evidência suficiente                                     |

---

# 🏗️ 4. Anatomia do Sistema

O Sunsix Linux não deve ser entendido como um sistema construído integralmente do zero.

A arquitetura observada indica uma distribuição OEM baseada na infraestrutura do Ubuntu:

```text
Sunsix Linux
│
├── 💿 Mídia ISO
│
├── 🚀 Bootloader
│
├── 🐧 Kernel Linux 2.6.20
│
├── ⚙️ initrd
│
├── 💾 Casper
│
├── 📦 filesystem.squashfs
│
├── 🐧 Base Ubuntu 7.04
│
├── 🖥️ GNOME 2.18
│
├── 📦 APT / dpkg
│
└── 💿 Ubiquity
    └── Instalação no disco
```

A investigação técnica procura determinar **quais partes dessa estrutura permanecem idênticas ao Ubuntu original e onde aparecem as alterações específicas da Sunsix**.

---

# 🟢 5. Evidências da Base Ubuntu

A identificação da mídia como baseada no **Ubuntu 7.04 Feisty Fawn** é sustentada por múltiplas características observadas:

* infraestrutura baseada em **Casper**;
* instalador gráfico **Ubiquity**;
* gerenciamento de pacotes através de **APT / dpkg**;
* kernel da geração **Linux 2.6.20**;
* ambiente gráfico da geração **GNOME 2.18**;
* conjunto de pacotes compatível com o Ubuntu Feisty.

A combinação desses elementos forma uma evidência consistente de que o Sunsix Linux foi construído a partir de uma base Ubuntu 7.04.

---

# 📦 6. O Inventário de Pacotes

A análise do manifesto de pacotes revelou um sistema fortemente compatível com o ecossistema Ubuntu Feisty.

Entre os componentes identificados estão versões compatíveis com a época de:

* Firefox 2.0.0.x;
* OpenOffice.org 2.2;
* GNOME 2.18;
* kernel Linux 2.6.20;
* componentes Flash da época;
* pacotes de idioma;
* atualizações relacionadas à geração Feisty.

Alguns pacotes incomuns também aparecem no inventário, incluindo componentes como:

```text
smartdimmer
toshset
```

No entanto, a simples presença desses pacotes **não é evidência de que sejam software desenvolvido pela Sunsix**.

A classificação correta exige comparação direta com uma mídia Ubuntu 7.04 i386 de referência.

---

# 🕵️ 7. Onde Está o Sunsix?

Esta é atualmente a principal pergunta da investigação.

A busca por arquivos contendo explicitamente o nome `sunsix` não encontrou resultados:

```bash
unsquashfs -l filesystem.squashfs | grep -i sunsix
```

Isso **não significa que a customização OEM esteja ausente**.

Uma distribuição OEM pode modificar arquivos existentes sem alterar seus nomes.

A identidade da Sunsix pode estar escondida em:

```text
SUNSIX LINUX
│
├── 🐧 Base Ubuntu 7.04
│
├── 🖥️ GNOME 2.18
│
├── 🐧 Kernel Linux
│
└── 🔍 Camada OEM Sunsix
    │
    ├── 🎨 Wallpapers
    ├── 🖼️ Artwork
    ├── 🎭 Temas GNOME
    ├── 👤 Configurações de usuário
    ├── 🔐 Tela de login
    ├── 🚀 Boot splash
    ├── ⚙️ Configurações padrão
    ├── 📦 Seleção de pacotes
    ├── 🛠️ Scripts OEM
    └── 💿 Customização do instalador
```

A ausência da palavra "Sunsix" nos nomes dos arquivos não elimina nenhuma dessas possibilidades.

---

# 🔍 8. Áreas Sob Investigação

A procura pela camada OEM deve examinar diferentes regiões do sistema.

| Camada        | Locais relevantes                                           |
| ------------- | ----------------------------------------------------------- |
| ISO / Boot    | `isolinux/`, menu, parâmetros, splash, Volume ID, El Torito |
| Live System   | `casper/`, `filesystem.squashfs`, `initrd`                  |
| Identidade    | `/etc/lsb-release`, `/etc/issue`, `/etc/issue.net`          |
| APT           | `/etc/apt/sources.list` e repositórios                      |
| Pacotes       | `/var/lib/dpkg/status`, `/var/lib/dpkg/info/`               |
| GNOME         | `/etc/gconf/`, menus e configurações                        |
| GDM           | `/etc/gdm/` e recursos da tela de login                     |
| X.Org         | `/etc/X11/`                                                 |
| Artwork       | `/usr/share/backgrounds/`, `pixmaps/`, `icons/`, `themes/`  |
| Boot Splash   | `/usr/lib/usplash/`, `/etc/usplash.conf`                    |
| Ubiquity      | `/usr/share/ubiquity/`                                      |
| Scripts OEM   | `/opt/`, `/usr/local/`, `/etc/init.d/`                      |
| Perfil padrão | `/etc/skel/`                                                |

Cada arquivo ou diretório diferente do Ubuntu original poderá representar uma possível evidência da camada OEM.

---

# 💡 9. Hipótese Atual

> **Hipótese de trabalho:** o Sunsix Linux provavelmente foi produzido a partir de uma base Ubuntu 7.04 Feisty Fawn, com a maior parte de sua identidade OEM implementada através de configuração, artwork, seleção de pacotes e ajustes do ambiente gráfico.

Essa hipótese explica por que:

* não foram encontrados grandes conjuntos de pacotes nomeados "sunsix";
* a arquitetura permanece fortemente compatível com o Ubuntu original;
* a personalização pode estar distribuída em arquivos genéricos do sistema;
* componentes Ubuntu podem ter sido modificados sem mudança de nome.

A hipótese será testada através de comparação direta com uma mídia Ubuntu 7.04 i386 original.

---

# 🧪 10. Experimentos Realizados

## Busca por referências explícitas à Sunsix

### Comando

```bash
unsquashfs -l filesystem.squashfs | grep -i sunsix
```

### Resultado

Nenhuma referência explícita à palavra `sunsix` foi encontrada nos nomes listados.

### Conclusão

🟡 A customização não parece depender de arquivos explicitamente nomeados com a marca.

---

## Análise da estrutura do sistema

### Resultado

A mídia apresenta uma estrutura compatível com:

* Casper;
* SquashFS;
* kernel Linux 2.6.20;
* GNOME 2.18;
* Ubiquity;
* APT / dpkg.

### Conclusão

🟢 O sistema possui forte compatibilidade arquitetural com o Ubuntu 7.04.

---

## Análise do manifesto de pacotes

### Resultado

O inventário apresenta versões e componentes característicos da geração Ubuntu Feisty.

### Conclusão

🟢 A análise reforça a identificação da base Ubuntu 7.04.

---

# 🗺️ 11. Mapa de Evidências

| Descoberta                            | Fonte                          | Estado |
| ------------------------------------- | ------------------------------ | ------ |
| Arquitetura i386                      | Mídia analisada                | 🟢     |
| Ubuntu 7.04                           | Estrutura e pacotes            | 🟢     |
| GNOME 2.18                            | Componentes instalados         | 🟢     |
| Kernel 2.6.20                         | Ambiente e pacotes             | 🟢     |
| Casper                                | Estrutura da ISO               | 🟢     |
| Ubiquity                              | Sistema analisado              | 🟢     |
| Customização OEM                      | Branding e contexto da mídia   | 🟡     |
| Customização por artwork/configuração | Evidências técnicas            | 🟡     |
| Autor da customização                 | Nenhuma evidência identificada | 🔴     |
| Data exata da ISO                     | Ainda não determinada          | 🔴     |
| Outras versões da mídia               | Ainda em investigação          | 🔴     |

---

# 📚 12. Evidências Históricas Externas

Além da análise da mídia, existem evidências históricas de que computadores Sunsix foram comercializados no Brasil com Linux pré-instalado.

Registros e anúncios da época associam computadores da marca a:

* processadores Intel e AMD;
* memória DDR2;
* discos rígidos SATA;
* sistemas Linux.

Também existem relatos que associam explicitamente computadores Sunsix ao **Ubuntu Linux** e ao **Ubuntu 7.04 Feisty Fawn**.

Essas evidências externas reforçam a hipótese de que a mídia preservada represente uma customização OEM baseada no Ubuntu.

> 🔵 Evidências históricas externas são utilizadas como apoio contextual e não substituem evidências encontradas diretamente na mídia.

---

# 🔬 13. Estado Atual da Investigação

## Preservado

* 🟢 ISO original;
* 🟢 SHA-256 registrado;
* 🟢 Arquitetura identificada;
* 🟢 Execução virtual possível.

## Identificado

* 🟢 Ubuntu 7.04 Feisty Fawn;
* 🟢 GNOME 2.18;
* 🟢 Kernel 2.6.20 / série 2.6.20-15;
* 🟢 APT / dpkg;
* 🟢 Casper;
* 🟢 Ubiquity.

## Em investigação

* 🟡 Lista completa de pacotes;
* 🟡 diferenças em relação ao Ubuntu original;
* 🟡 customizações OEM;
* 🟡 seleção de pacotes;
* 🟡 artwork;
* 🟡 hardware originalmente associado à mídia.

## Procurando

* 🔍 Documentação original;
* 🔍 outras versões da ISO;
* 🔍 CD de drivers e extras;
* 🔍 manuais;
* 🔍 fotografias;
* 🔍 registros de computadores Sunsix.

---

# ❓ 14. Perguntas Abertas

Ainda precisamos descobrir:

* Qual é a data exata de criação da ISO?
* Esta mídia corresponde ao primeiro release ou a uma revisão posterior?
* Quem produziu a customização OEM?
* Quais arquivos foram modificados em relação ao Ubuntu original?
* Existem pacotes próprios com nomes neutros?
* Existem scripts ou binários exclusivos?
* Quais computadores receberam essa mídia?
* Existia mais de uma versão do Sunsix Linux?
* O CD azul correspondia ao sistema principal?
* Existia um CD laranja separado para drivers e extras?
* Existem manuais ou documentos originais?
* Como a mídia era distribuída junto aos computadores?
* Quais wallpapers, temas, sons e ícones eram exclusivos?

---

# 🚀 15. Próxima Etapa da Investigação

A próxima etapa prioritária é obter uma mídia de referência:

```text
Ubuntu 7.04 Desktop i386
```

A comparação deverá seguir este processo:

```text
1. Preservar as ISOs originais
          ↓
2. Registrar checksums
          ↓
3. Extrair as estruturas
          ↓
4. Comparar arquivos
          ↓
5. Comparar pacotes
          ↓
6. Identificar diferenças
          ↓
7. Classificar diferenças
          ↓
8. Registrar evidências
```

As diferenças deverão ser classificadas como:

```text
OEM
Configuração
Artwork
Pacotes
Hardware
Instalação
Indeterminado
```

O objetivo é responder à principal pergunta da pesquisa:

> **O que transformou o Ubuntu 7.04 em Sunsix Linux?**

---

# 🧰 16. Metodologia de Preservação

A investigação segue os seguintes princípios:

1. Preservar a ISO original antes de qualquer manipulação.
2. Registrar checksums.
3. Trabalhar sempre sobre cópias.
4. Inventariar a estrutura antes de modificar ou extrair conteúdo.
5. Catalogar bootloader, kernel, initrd e arquivos de configuração.
6. Extrair o `filesystem.squashfs` para análise.
7. Registrar versões e nomes dos pacotes.
8. Comparar a mídia com uma referência Ubuntu original.
9. Examinar diferenças em `/etc`, `/usr/share`, `/opt` e `/usr/local`.
10. Investigar GNOME, GDM, X.Org e usplash.
11. Examinar scripts de instalação e pós-instalação.
12. Separar fatos, inferências e hipóteses.
13. Registrar hashes e caminhos dos arquivos relevantes.
14. Manter todos os resultados reproduzíveis.

---

# 🔒 17. Segurança

O Sunsix Linux é um sistema extremamente antigo.

Ele **não deve ser utilizado como sistema operacional principal nem conectado diretamente à Internet**.

Para análise e experimentação, recomenda-se:

* utilizar máquinas virtuais;
* manter a rede desativada ou isolada;
* utilizar snapshots;
* evitar dados pessoais;
* manter a ISO original intacta.

> **O objetivo deste projeto é preservação histórica e pesquisa técnica.**

---

# 📚 Referências

* [Repositório Sunsix Linux](https://github.com/gushpat/sunsix-linux)
* [Ubuntu 7.04 — Old Releases](https://old-releases.ubuntu.com/releases/7.04/)
* [Ubuntu 7.04 Beta — Informações técnicas históricas](https://ubuntu.com/blog/ubuntu-7-04-beta)

---

