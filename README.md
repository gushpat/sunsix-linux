# 🐧 Sunsix Linux — OEM Edition

<p align="center">
  <img src="assets/images/sunsixos.webp" alt="Sunsix Linux" width="180">
</p>

<p align="center">
  <strong>Preservando uma distribuição Linux brasileira dos anos 2000.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Preservado-success">
  <img src="https://img.shields.io/badge/Arquitetura-i386-blue">
  <img src="https://img.shields.io/badge/Base-Ubuntu%207.x-orange">
  <img src="https://img.shields.io/badge/Era-2007%E2%80%932008-lightgrey">
</p>

---

## 📖 Sobre o projeto

O **Sunsix Linux** foi uma distribuição GNU/Linux brasileira desenvolvida para computadores OEM da marca **Sunsix**, comercializados no Brasil durante a segunda metade dos anos 2000.

Este repositório tem como objetivo **preservar, documentar e tornar acessível esse pedaço da história da computação brasileira**.

A mídia preservada neste projeto corresponde a uma versão original do sistema distribuída com computadores Sunsix. O objetivo não é desenvolver uma nova distribuição, mas manter o registro de um software que fez parte da experiência de milhares de computadores vendidos no varejo brasileiro durante a era do Windows XP, dos processadores Core 2 Duo e dos primeiros computadores populares equipados com Linux.

O projeto pode ser utilizado para:

- 🏛️ Preservação histórica e arqueologia digital
- 💿 Estudo de distribuições Linux antigas
- 🖥️ Retrocomputação
- 🧪 Pesquisa e experimentação
- 🎮 Emulação e virtualização
- 📚 Documentação de software brasileiro
- 🧑‍💻 Curiosidade e nostalgia

> **Este projeto é uma iniciativa de preservação.**
>
> O Sunsix Linux não deve ser considerado uma distribuição moderna ou indicada para uso cotidiano.

---

## 🏪 Contexto histórico

Durante a década de 2000, fabricantes brasileiros de computadores começaram a oferecer máquinas equipadas com GNU/Linux como alternativa aos computadores vendidos com licenças proprietárias.

A Sunsix esteve entre as marcas que comercializavam computadores com Linux pré-instalado, especialmente através de grandes redes varejistas brasileiras.

Entre os pontos de venda associados a esse período estavam redes como:

- Lojas Americanas
- Extra
- Walmart

As máquinas eram direcionadas principalmente ao mercado doméstico e de entrada, oferecendo configurações que, para a época, apresentavam uma boa relação entre preço e desempenho.

Entre os equipamentos encontrados nesse período estavam computadores equipados com processadores **Intel Celeron** e **Intel Core 2 Duo**, memória DDR2 e discos rígidos SATA.

O Sunsix Linux fazia parte dessa experiência: um sistema baseado em uma distribuição Linux conhecida, mas adaptado visualmente para acompanhar a identidade dos computadores vendidos pela marca.

---

## 💿 A ISO preservada

A imagem de instalação preservada neste repositório corresponde à mídia original do Sunsix Linux.

### Informações conhecidas

| Informação | Detalhe |
|---|---|
| Distribuição | Sunsix Linux |
| Tipo | OEM / distribuição pré-instalada |
| Arquitetura | i386 / x86 — 32 bits |
| Mídia original | CD-ROM |
| Tamanho aproximado | ~650 MB |
| Base | Ubuntu 7.x |
| Interface | GNOME 2.x |
| Sistema de pacotes | APT |
| Período aproximado | 2007–2008 |

> ⚠️ Algumas informações ainda estão sendo investigadas. Sempre que possível, este repositório busca distinguir informações confirmadas diretamente pela mídia de informações obtidas através de relatos e documentação histórica.

---

## 📦 Download da ISO

A imagem de instalação do Sunsix Linux está disponível na seção **Releases** deste repositório.

👉 **[Baixar o Sunsix Linux](../../releases)**

### Arquivo

```text
sunsix-linux.iso
```

### SHA-256

Utilize o SHA-256 abaixo para verificar a integridade da imagem:

```text
COLOCAR_SHA256_DA_ISO_AQUI
```

> 💡 **Importante:** se você possui uma mídia física original do Sunsix Linux e obtiver um checksum diferente, não descarte essa cópia. Uma diferença pode indicar uma versão ou revisão diferente da mídia e pode ser relevante para a preservação histórica.

---

## 🛠️ Especificações Técnicas Legadas

O Sunsix Linux representa uma geração bastante diferente das distribuições GNU/Linux atuais.

### Sistema

- **Arquitetura:** i386 / x86 32-bit
- **Kernel:** série Linux 2.6.x
- **Desktop:** GNOME 2.x
- **Sistema de pacotes:** APT / dpkg
- **Sistema base:** Ubuntu 7.x
- **Mídia:** CD-ROM
- **Firmware esperado:** BIOS tradicional

### Hardware de época

Os computadores Sunsix comercializados durante esse período utilizavam configurações compatíveis com a tecnologia disponível na época, incluindo:

- Intel Celeron
- Intel Core 2 Duo
- 1 GB a 2 GB de memória DDR2
- HDs SATA
- Unidade óptica CD/DVD
- BIOS tradicional
- Chipsets e controladoras da geração Intel Core 2

Um exemplo de configuração encontrada em computadores dessa época inclui o:

**Intel Core 2 Duo E4500 — 2.2 GHz**

> ⚠️ As configurações variavam de acordo com o modelo do computador. Os dados acima representam hardware encontrado ou compatível com máquinas da época e não devem ser interpretados como a configuração universal de todos os computadores Sunsix.

---

## ⚠️ Resolução de Problemas no Boot

O Sunsix Linux possui um kernel extremamente antigo para os padrões atuais.

Dependendo do chipset da placa-mãe, controlador de armazenamento, BIOS ou unidade óptica utilizada, o sistema pode apresentar problemas durante o processo de inicialização.

Um dos problemas encontrados pode resultar em uma mensagem semelhante a:

```text
Alert! /dev/disk/by-uuid/XXXX-XXXX does not exist.
Dropping to a shell!

Cant access tty; job control turned off

(initramfs) _
```

Esse erro indica que o sistema não conseguiu localizar o dispositivo necessário durante o processo de inicialização.

### Como solucionar

Em determinadas configurações de hardware antigo, pode ser possível contornar o problema utilizando parâmetros adicionais do kernel.

1. Na primeira tela de inicialização do CD, acesse as opções avançadas.
2. Pressione **F6**, quando disponível.
3. Localize a linha contendo os parâmetros de inicialização do kernel.
4. Vá até o final da linha.
5. Adicione um espaço e insira:

```text
all_generic_ide irqpoll acpi=off
```

6. Pressione **Enter** para iniciar o sistema.

### O que esses parâmetros fazem?

**`all_generic_ide`**

Força o kernel a utilizar mecanismos IDE genéricos, podendo ajudar em determinadas combinações antigas de controladoras e dispositivos de armazenamento.

**`irqpoll`**

Modifica o tratamento de interrupções de hardware e pode ajudar em determinados problemas relacionados a IRQs.

**`acpi=off`**

Desativa o ACPI — Advanced Configuration and Power Interface.

Isso pode contornar problemas de compatibilidade entre o kernel antigo e determinadas implementações de BIOS, mas também desativa funcionalidades relacionadas ao gerenciamento de energia.

> ⚠️ Esses parâmetros são soluções de compatibilidade e não devem ser utilizados sem necessidade.

---

## 💻 Como Executar Atualmente

Devido à idade do sistema, **a virtualização é a maneira mais recomendada de experimentar o Sunsix Linux atualmente**.

Não é necessário possuir um computador Sunsix original.

Hardware moderno pode apresentar incompatibilidades devido à ausência de suporte no kernel original para tecnologias introduzidas posteriormente.

Entre os problemas esperados estão:

- UEFI
- Secure Boot
- USB 3.x
- Hardware gráfico moderno
- Controladoras de armazenamento recentes
- CPUs e chipsets muito posteriores à época da distribuição

Para preservar melhor o ambiente original, recomenda-se utilizar uma máquina virtual que simule hardware compatível com a época.

### VirtualBox

Crie uma máquina virtual com aproximadamente estas configurações:

| Configuração | Valor |
|---|---|
| Sistema | Linux |
| Arquitetura | 32 bits |
| Memória RAM | 512 MB – 1024 MB |
| CPU | 1 núcleo |
| Disco virtual | IDE |
| Unidade óptica | CD/DVD |
| Firmware | BIOS / Legacy |
| Rede | Intel PRO/1000 ou PCnet |

#### Passo a passo

1. Abra o VirtualBox.
2. Crie uma nova máquina virtual.
3. Selecione **Linux** como sistema operacional.
4. Escolha uma configuração de **32 bits**.
5. Atribua entre **512 MB e 1024 MB de RAM**.
6. Configure o armazenamento utilizando um controlador IDE.
7. Monte a ISO do Sunsix Linux como unidade de CD/DVD.
8. Certifique-se de que o firmware utilizado seja BIOS/Legacy.
9. Inicie a máquina virtual.

> 💡 Para sistemas Linux tão antigos, utilizar uma quantidade excessiva de memória ou dispositivos virtuais modernos pode causar problemas inesperados.

---

## 🐧 Inicialização Rápida via QEMU

O QEMU permite executar rapidamente a ISO utilizando uma máquina virtual x86.

### LiveCD

```bash
qemu-system-i386 \
  -m 512M \
  -cdrom sunsix-linux.iso \
  -boot d
```

Para aproximar ainda mais o ambiente de um computador antigo:

```bash
qemu-system-i386 \
  -m 512M \
  -cpu pentium3 \
  -cdrom sunsix-linux.iso \
  -boot d
```

---

## 💽 Instalando em um Disco Virtual

Também é possível instalar o Sunsix Linux em um disco virtual.

Primeiro, crie uma imagem de disco:

```bash
qemu-img create -f qcow2 sunsix.qcow2 8G
```

Depois inicialize a ISO:

```bash
qemu-system-i386 \
  -m 512M \
  -cpu pentium3 \
  -hda sunsix.qcow2 \
  -cdrom sunsix-linux.iso \
  -boot d
```

O sistema poderá então ser instalado dentro do disco virtual como seria feito em um computador físico.

Depois da instalação, o disco virtual poderá ser iniciado sem a ISO:

```bash
qemu-system-i386 \
  -m 512M \
  -cpu pentium3 \
  -hda sunsix.qcow2
```

---

## 📸 Capturas de Tela

Substitua os arquivos abaixo por capturas reais do sistema:

| Tela de Inicialização | Desktop Sunsix | Informações do Sistema |
|:---:|:---:|:---:|
| ![Boot](screenshots/boot.png) | ![Desktop](screenshots/desktop.png) | ![System Info](screenshots/system-info.png) |

Quando possível, as capturas devem ser realizadas utilizando:

- A ISO original;
- Uma instalação reproduzida em ambiente virtual;
- Hardware original ou compatível com a época.

---

## 🔬 Estado da Preservação

Este projeto está sendo desenvolvido como um registro histórico da distribuição.

| Item | Estado |
|---|---|
| ISO original | ✅ Preservada |
| Arquitetura identificada | ✅ i386 |
| Ambiente virtual | ✅ Testável |
| QEMU | ✅ Testável |
| VirtualBox | ✅ Testável |
| Screenshots | 🔄 Em documentação |
| Lista completa de pacotes | 🔄 Em análise |
| Customizações OEM | 🔄 Em investigação |
| Hardware original | 🔄 Em investigação |
| Documentação original | 🔍 Procurando |
| Mídias alternativas | 🔍 Procurando |
| Checksum SHA-256 | 🔄 A confirmar |

---

## 🔎 O Que Já Sabemos

Até o momento, as informações identificadas incluem:

- O Sunsix Linux era utilizado em computadores OEM da marca Sunsix.
- A distribuição pertence à geração de Linux para computadores domésticos da segunda metade dos anos 2000.
- A mídia utiliza arquitetura x86 de 32 bits.
- O sistema possui forte relação com a família Ubuntu 7.x.
- A interface gráfica é baseada na geração GNOME 2.
- A distribuição contém personalizações visuais relacionadas à marca Sunsix.
- A mídia pode ser executada através de virtualização e emulação de hardware x86 antigo.
- A distribuição foi utilizada em computadores vendidos no mercado brasileiro.

---

## ❓ O Que Ainda Estamos Investigando

A preservação ainda está em andamento.

Algumas perguntas permanecem abertas:

- Qual é a versão exata do Ubuntu utilizada?
- Qual é a versão exata do kernel?
- Qual era a data de compilação da ISO?
- Quem desenvolveu a customização do Sunsix Linux?
- Quais pacotes foram adicionados ou modificados pela Sunsix?
- Qual era o modelo exato dos computadores distribuídos com essa versão?
- Existiam diferentes versões da ISO?
- Existem outras mídias originais ainda preservadas?
- Quais eram os papéis de parede, temas e aplicativos exclusivos da Sunsix?
- Existem manuais ou CDs de recuperação originais?
- Quais eram as configurações de fábrica das máquinas?
- Quais redes varejistas comercializavam cada modelo?
- Existiam versões diferentes do sistema para desktops e notebooks?

Toda nova evidência pode ajudar a responder essas perguntas.

---

## 🧪 Análise Técnica da ISO

Uma das metas deste projeto é documentar o conteúdo da ISO além da simples disponibilização do arquivo.

Entre os dados que podem ser analisados estão:

- Versão do kernel
- Versão exata do Ubuntu
- Lista de pacotes instalados
- Arquivos de configuração
- Temas GTK
- Wallpapers
- Aplicativos OEM
- Scripts de inicialização
- Informações do GRUB
- Data de criação dos arquivos
- Identificação do hardware suportado
- Configuração de rede
- Configuração gráfica
- Serviços iniciados durante o boot
- Personalizações realizadas pela Sunsix

Os resultados dessas análises poderão ser adicionados ao diretório:

```text
docs/
```

---

## 🗂️ Estrutura do Repositório

A estrutura planejada é:

```text
sunsix-linux/
├── README.md
├── LICENSE
├── SHA256SUMS
├── assets/
│   └── sunsix-logo.png
├── screenshots/
│   ├── boot.png
│   ├── desktop.png
│   └── system-info.png
├── docs/
│   ├── history.md
│   ├── hardware.md
│   ├── technical-analysis.md
│   ├── boot.md
│   └── preservation.md
└── metadata/
    └── iso-info.txt
```

A ISO em si pode ser distribuída através da seção **Releases**, mantendo o código, documentação e arquivos auxiliares organizados.

---

## 📋 Metadados da Mídia

À medida que a análise avançar, os seguintes dados deverão ser registrados:

| Propriedade | Valor |
|---|---|
| Nome do arquivo | `sunsix-linux.iso` |
| Tamanho | A confirmar |
| SHA-256 | A confirmar |
| MD5 | A confirmar |
| Arquitetura | i386 |
| Sistema base | Ubuntu 7.x |
| Kernel | A confirmar |
| Data de criação | A confirmar |
| Data de modificação | A confirmar |
| Tipo de mídia | CD-ROM |
| Método de aquisição | A documentar |

---

## 🧰 Ferramentas para Análise

Algumas ferramentas úteis para análise da mídia incluem:

### Identificação do arquivo

```bash
file sunsix-linux.iso
```

### SHA-256

```bash
sha256sum sunsix-linux.iso
```

### MD5

```bash
md5sum sunsix-linux.iso
```

### Informações da ISO

```bash
isoinfo -d -i sunsix-linux.iso
```

### Listagem do conteúdo

```bash
isoinfo -l -i sunsix-linux.iso
```

Esses dados podem ser registrados em:

```text
metadata/iso-info.txt
```

---

## 🤝 Contribua para o Resgate da História do Linux no Brasil

Você trabalhou na montagem desses computadores?

Possui informações sobre o Sunsix Linux?

Talvez você tenha:

- 💿 O CD original
- 💻 Um computador Sunsix antigo
- 📦 A caixa original
- 📖 Um manual
- 📸 Fotografias
- 🧾 Notas fiscais antigas
- 💾 Drivers
- 💿 CDs de recuperação
- 🖥️ Outra versão da ISO
- 📝 Anotações
- 🧠 Memórias de ter utilizado o sistema
- 🏢 Informações sobre a empresa ou equipe responsável pelo software

**Não descarte esse material.**

Mesmo uma fotografia antiga ou um relato aparentemente pequeno pode ajudar a reconstruir a história dessa distribuição.

### Como contribuir

Você pode:

1. Abrir uma **Issue** com informações ou relatos.
2. Enviar fotografias e documentação.
3. Comparar outra mídia com a ISO preservada.
4. Relatar testes realizados em hardware real.
5. Enviar um Pull Request com documentação.
6. Compartilhar informações sobre computadores Sunsix encontrados.
7. Informar sobre outras cópias da ISO existentes.

> 🔎 Se você possuir outra imagem ISO, não substitua a existente imediatamente. Primeiro registre seu tamanho, checksum e origem. Duas imagens aparentemente iguais podem representar versões diferentes da mídia.

---

## 🏛️ Preservação Digital

Software antigo desaparece facilmente.

Sites ficam offline, empresas encerram atividades, CDs são descartados e computadores antigos deixam de funcionar.

Projetos como este procuram evitar que essas pequenas partes da história da computação desapareçam completamente.

O Sunsix Linux é especialmente interessante por representar um período em que **computadores brasileiros vendidos em grandes redes de varejo chegaram às casas dos consumidores equipados com GNU/Linux**.

Preservar a ISO significa preservar não apenas um sistema operacional, mas também uma pequena parte da história da informática brasileira.

---

## 📚 Por Que Preservar Software OEM?

Distribuições OEM frequentemente recebem pouca atenção histórica.

Grandes distribuições como Ubuntu, Debian, Fedora e Mandriva possuem extensa documentação, mirrors, fóruns e comunidades.

Já versões personalizadas por fabricantes podem desaparecer rapidamente.

Quando o computador deixa de ser comercializado, o site do fabricante pode sair do ar, os servidores de download podem desaparecer e os CDs podem acabar em caixas antigas ou serem descartados.

O Sunsix Linux representa justamente esse tipo de software.

A distribuição pode ter sido utilizada por milhares de pessoas e, ainda assim, possuir pouquíssima documentação disponível atualmente.

Este projeto procura preservar essa memória.

---

## ⚖️ Licença e Notas Legais

Este repositório possui finalidade de **preservação histórica, documentação, pesquisa e estudo**.

O Sunsix Linux é composto por software proveniente de diferentes projetos e seus respectivos detentores de direitos.

Os componentes distribuídos sob licenças livres continuam sujeitos às suas respectivas licenças.

A presença da marca **Sunsix** neste projeto não representa reivindicação de propriedade sobre a marca ou seus elementos visuais.

A marca, logotipos, imagens proprietárias e demais materiais pertencem aos seus respectivos detentores de direitos.

> A disponibilização de material histórico neste repositório não implica que o projeto reivindique a propriedade intelectual dos componentes de terceiros.

Caso você seja o detentor de direitos sobre algum material disponibilizado neste projeto e acredite que sua utilização esteja inadequada, entre em contato através das ferramentas de comunicação disponíveis no GitHub para que a situação possa ser analisada.

---

## 🔒 Aviso sobre Software Legado

O Sunsix Linux é um sistema operacional extremamente antigo e **não deve ser utilizado como sistema principal conectado à Internet**.

O sistema contém componentes que estão há muitos anos sem atualizações de segurança.

Para fins de experimentação, recomenda-se:

- Utilizar uma máquina virtual;
- Evitar dados pessoais;
- Evitar conectar o sistema diretamente à Internet;
- Preferir redes isoladas;
- Utilizar snapshots da máquina virtual;
- Manter a ISO original intacta.

> 🔒 **Este projeto é voltado para preservação e estudo, não para uso seguro em produção.**

---

## ❤️ Ajude a Preservar

Se você encontrou este repositório porque também se lembra do Sunsix Linux, considere compartilhar sua história.

Talvez você tenha utilizado um desses computadores na infância.

Talvez tenha sido seu primeiro contato com Linux.

Talvez aquele computador Sunsix ainda esteja guardado em algum lugar.

Talvez você ainda tenha o CD original em uma gaveta.

**Se você ainda possui alguma evidência dessa época, ela pode ajudar a preservar essa história.**

---

<p align="center">
  <img src="assets/images/sunsixos.webp" alt="Sunsix Linux" width="120">
</p>

<p align="center">
  <strong>🐧 Sunsix Linux</strong><br>
  <sub>Uma pequena parte da história do Linux no Brasil.</sub>
</p>
