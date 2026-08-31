# 🐧 Sunsix Linux

<p align="center">
  <img src="assets/images/sunsixos.webp" alt="Sunsix Linux" width="180">
</p>

<p align="center">
  <strong>Preservando um pedaço esquecido da história da computação brasileira.</strong>
</p>

<p align="center">
  Uma distribuição Linux OEM brasileira da era do Windows XP.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Preservado-success">
  <img src="https://img.shields.io/badge/Arquitetura-i386-blue">
  <img src="https://img.shields.io/badge/Base-Ubuntu%207.x-orange">
  <img src="https://img.shields.io/badge/Era-2007%E2%80%932008-lightgrey">
</p>

---

## 📖 Sobre

O **Sunsix Linux** é uma distribuição GNU/Linux brasileira associada aos computadores OEM da marca **Sunsix**, comercializados no Brasil durante a segunda metade dos anos 2000.

Este projeto existe para **preservar, documentar e estudar** esse software e o contexto em que ele foi distribuído.

A ISO preservada corresponde a uma mídia original do sistema e representa um exemplo da presença do Linux em computadores domésticos brasileiros durante a era do Windows XP.

> 🏛️ **Este é um projeto de preservação digital, não uma nova distribuição Linux.**

---

## 📋 At a Glance

|                         |                              |
| ----------------------- | ---------------------------- |
| 🐧 **Sistema**          | Sunsix Linux                 |
| 🇧🇷 **Origem**         | Brasil                       |
| 📅 **Período estimado** | 2007–2008                    |
| 💿 **Mídia**            | CD-ROM                       |
| 🧬 **Base**             | Ubuntu 7.x                   |
| 🖥️ **Desktop**         | GNOME 2.x                    |
| ⚙️ **Arquitetura**      | i386 / 32-bit                |
| 📦 **Gerenciador**      | APT / dpkg                   |
| 🔬 **Status**           | Preservado e em investigação |

> Algumas informações ainda estão sendo verificadas. O projeto diferencia evidências encontradas diretamente na mídia de informações obtidas através de relatos e documentação histórica.

---

## 📦 ISO Preservada

Em breve, a imagem original estará disponível através das **Releases** do projeto.

<!--
**[⬇️ Baixar o Sunsix Linux](../../releases)**

```text
sunsix-linux.iso
```
-->
### Integridade

```text
SHA-256: A CONFIRMAR
```

> 💡 Se você possui outra mídia do Sunsix Linux e obtiver um checksum diferente, **não descarte a cópia**. Ela pode representar uma versão ou revisão diferente e ser importante para a preservação.

---

## 🏛️ Um pedaço da história do Linux no Brasil

Durante os anos 2000, computadores vendidos no Brasil começaram a chegar ao consumidor com GNU/Linux pré-instalado como alternativa aos sistemas proprietários.

O Sunsix Linux faz parte desse período.

A distribuição foi associada a computadores de entrada e domésticos vendidos durante uma época marcada por:

* Windows XP;
* processadores Intel Celeron e Core 2 Duo;
* memória DDR2;
* discos rígidos SATA;
* monitores LCD;
* CDs de instalação e recuperação;
* expansão do acesso a computadores domésticos.

O objetivo deste projeto é preservar **não apenas a ISO**, mas também o contexto em que ela existiu.

---

## 🔎 O Que Sabemos

Até o momento, a análise da mídia e das evidências disponíveis indica:

* Arquitetura **i386 / x86 32-bit**;
* Ambiente baseado na geração **Ubuntu 7.x**;
* Desktop baseado no **GNOME 2.x**;
* Sistema de pacotes **APT / dpkg**;
* Personalizações visuais relacionadas à marca Sunsix;
* Distribuição em mídia **CD-ROM**;
* Compatibilidade com computadores x86 da época.

A investigação continua.

---

## 🕵️ O Que Ainda Estamos Investigando

Algumas perguntas permanecem abertas:

* Qual é a versão exata do Ubuntu?
* Qual é a versão exata do kernel?
* Quando a ISO foi criada?
* Quem desenvolveu a customização?
* Quais componentes foram modificados pela Sunsix?
* Quais modelos de computadores receberam o sistema?
* Existiam outras versões da ISO?
* Existem CDs de recuperação ou mídias alternativas?
* Quais eram os aplicativos e temas exclusivos?
* Existem manuais ou documentos originais?
* Qual era a distribuição exata através do varejo brasileiro?

**Cada nova evidência pode ajudar a responder essas perguntas.**

---

## 🧪 Evidências e Nível de Confiança

Para evitar que hipóteses sejam confundidas com fatos, o projeto utiliza diferentes níveis de evidência:

| Símbolo | Significado                                                |
| ------- | ---------------------------------------------------------- |
| 🟢      | Confirmado diretamente pela mídia ou documentação primária |
| 🟡      | Provável, baseado em múltiplas evidências                  |
| 🔵      | Relato ou informação histórica de terceiros                |
| 🔴      | Ainda desconhecido                                         |

A documentação detalhada das evidências e descobertas será mantida em [`docs/`](docs/).

---

## 🖥️ Executando o Sunsix Linux

Devido à idade do sistema, a maneira mais simples de experimentá-lo atualmente é através de **virtualização ou emulação de hardware x86 antigo**.

### QEMU

Uma execução básica da ISO:

```bash
qemu-system-i386 \
  -m 512M \
  -cdrom sunsix-linux.iso \
  -boot d
```

Para aproximar o ambiente de computadores antigos:

```bash
qemu-system-i386 \
  -m 512M \
  -cpu pentium3 \
  -cdrom sunsix-linux.iso \
  -boot d
```

### VirtualBox

Configuração recomendada:

| Configuração   | Valor            |
| -------------- | ---------------- |
| Sistema        | Linux            |
| Arquitetura    | 32 bits          |
| RAM            | 512 MB – 1024 MB |
| CPU            | 1 núcleo         |
| Armazenamento  | IDE              |
| Firmware       | BIOS / Legacy    |
| Unidade óptica | CD/DVD           |

📚 **Guias detalhados:** [`docs/`](docs/)

---

## ⚠️ Compatibilidade

O Sunsix Linux utiliza software desenvolvido para computadores de aproximadamente duas décadas atrás.

Hardware moderno pode apresentar problemas relacionados a:

* UEFI;
* Secure Boot;
* USB 3.x;
* GPUs modernas;
* controladoras de armazenamento;
* chipsets recentes;
* CPUs posteriores à geração suportada pelo kernel.

Problemas específicos de inicialização e compatibilidade estão documentados em:

[`docs/troubleshooting.md`](docs/troubleshooting.md)

---

## 📸 O Sistema

Capturas do ambiente original serão adicionadas conforme a documentação avançar.

<p align="center">
  <img src="screenshots/desktop.png" alt="Desktop do Sunsix Linux" width="800">
</p>

*Desktop do Sunsix Linux — captura pendente de documentação.*

---
<!-- Este texto ou código não será renderizado 

## 🗂️ Estrutura

```text
sunsix-linux/
├── README.md
├── LICENSE
├── SHA256SUMS
│
├── assets/
│   └── images/
│       └── sunsixos.webp
│
├── screenshots/
│   ├── boot.png
│   ├── desktop.png
│   └── system-info.png
│
├── docs/
│   ├── history.md
│   ├── hardware.md
│   ├── technical-analysis.md
│   ├── troubleshooting.md
│   └── preservation.md
│
└── metadata/
    └── iso-info.txt
```

A ISO é distribuída através da seção **Releases**, mantendo o repositório principal dedicado à documentação e preservação.

---
-->
## 🔬 Estado da Preservação

| Item                     | Estado             |
| ------------------------ | ------------------ |
| 💿 ISO original          | ✅ Preservada       |
| ⚙️ Arquitetura           | ✅ Identificada     |
| 🖥️ Ambiente virtual     | ✅ Testável         |
| 🐧 QEMU                  | ✅ Testável         |
| 📦 VirtualBox            | ✅ Testável         |
| 📸 Screenshots           | 🔄 Em documentação |
| 📋 Lista de pacotes      | 🔄 Em análise      |
| 🎨 Customizações OEM     | 🔄 Em investigação |
| 🖥️ Hardware original    | 🔄 Em investigação |
| 📖 Documentação original | 🔍 Procurando      |
| 💿 Mídias alternativas   | 🔍 Procurando      |
| 🔐 SHA-256               | 🔄 A confirmar     |

---

## 📚 Documentação

A investigação detalhada está sendo organizada separadamente:

* 📜 [`history.md`](docs/history.md) — contexto histórico
* 🖥️ [`hardware.md`](docs/hardware.md) — hardware e computadores da época
* 🔬 [`technical-analysis.md`](docs/technical-analysis.md) — análise da ISO
* 🛠️ [`troubleshooting.md`](docs/troubleshooting.md) — problemas de compatibilidade
* 🏛️ [`preservation.md`](docs/preservation.md) — metodologia de preservação

---

## 🤝 Ajude a Preservar

Você possui alguma lembrança ou material relacionado ao Sunsix?

Talvez ainda tenha:

* 💿 Um CD original;
* 💻 Um computador Sunsix;
* 📦 A caixa;
* 📖 Um manual;
* 📸 Fotografias;
* 💾 Drivers;
* 💿 CDs de recuperação;
* 📝 Documentos;
* 🧠 Relatos de utilização;
* 🖥️ Outra versão da ISO.

**Não descarte esse material.**

Mesmo uma fotografia ou pequeno relato pode fornecer uma pista importante.

### Como contribuir

Você pode:

1. Abrir uma **Issue**;
2. Enviar fotografias ou documentação;
3. Relatar testes realizados em hardware real;
4. Comparar outra mídia com a ISO preservada;
5. Enviar Pull Requests com documentação;
6. Informar sobre computadores Sunsix encontrados;
7. Compartilhar outras cópias da mídia.

> 🔎 Ao encontrar outra ISO, registre primeiro **origem, tamanho e checksum**. Não substitua ou descarte a cópia existente.

---

## 🏛️ Por Que Preservar?

Software OEM costuma desaparecer sem deixar muitos registros.

Empresas encerram atividades, sites ficam offline, servidores são desligados e CDs acabam sendo descartados.

Grandes distribuições possuem comunidades e arquivos históricos. Já sistemas personalizados por fabricantes podem desaparecer quase completamente.

O Sunsix Linux é um exemplo desse tipo de software.

Preservá-lo significa preservar uma pequena parte da história de como **o Linux chegou aos computadores domésticos brasileiros**.

---

## ⚖️ Licença e Direitos

Este projeto possui finalidade de **preservação histórica, documentação, pesquisa e estudo**.

O Sunsix Linux é composto por software proveniente de diferentes projetos e seus respectivos detentores de direitos.

Componentes distribuídos sob licenças livres permanecem sujeitos às suas respectivas licenças.

A marca **Sunsix**, seus logotipos e demais materiais proprietários pertencem aos seus respectivos detentores.

A existência deste projeto não implica reivindicação de propriedade sobre marcas, software ou materiais de terceiros.

Caso você seja detentor de direitos sobre algum material disponibilizado neste projeto e considere sua utilização inadequada, entre em contato através do GitHub.

---

## 🔒 Segurança

**Não utilize o Sunsix Linux como sistema operacional principal.**

O sistema contém componentes extremamente antigos e sem atualizações de segurança.

Para experimentação, recomendamos:

* 🖥️ Máquina virtual;
* 🔌 Rede isolada ou desativada;
* 🚫 Nenhum dado pessoal;
* 💾 Snapshots;
* 📀 Preservação da ISO original.

> **Este projeto é destinado à preservação e estudo, não ao uso cotidiano ou produção.**

---

## ❤️ Preserve Sua Cópia

Se você encontrou este projeto porque se lembra do Sunsix Linux, **compartilhe sua história**.

Talvez esse tenha sido seu primeiro computador.

Talvez tenha sido seu primeiro contato com Linux.

Talvez um antigo computador Sunsix ainda esteja guardado em algum lugar.

Ou talvez você ainda tenha aquele CD.

**Uma pequena evidência pode ajudar a reconstruir uma parte da história da computação brasileira.**

---

<p align="center">
  <img src="assets/images/sunsixos.webp" alt="Sunsix Linux" width="120">
</p>

<p align="center">
  <sub>Uma pequena parte da história do Linux no Brasil.</sub>
</p>
