# 🐧 Sunsix Linux

<p align="center">
  <img src="assets/images/sunsixos.webp" alt="Sunsix Linux" width="180">
</p>

<p align="center">
  <strong>Preservando um pedaço esquecido da história da computação brasileira.</strong>
</p>

<p align="center">
  Uma distribuição Linux OEM brasileira preservada como parte da história da computação nacional.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Preservado-success">
  <img src="https://img.shields.io/badge/Arquitetura-i386-blue">
  <img src="https://img.shields.io/badge/Base-Ubuntu 7.04 Feisty Fawn-orange">
  <img src="https://img.shields.io/badge/Era-2007%E2%80%932008-lightgrey">
</p>

---

## 📖 Sobre

O **Sunsix Linux** é uma distribuição GNU/Linux brasileira associada aos computadores OEM da marca **Sunsix**, comercializados no Brasil durante a segunda metade dos anos 2000.

Este projeto existe para **preservar, documentar e estudar** esse software e o contexto em que ele foi distribuído.

A ISO preservada corresponde a uma mídia original do sistema e representa um exemplo da presença do Linux em computadores domésticos brasileiros durante a era do Windows XP.

> 🏛️ **Este é um projeto de preservação digital, não uma nova distribuição Linux.**

---

## 📋 Em Resumo
|                      |             |
| ------------------------ | ------------------ |
| 🐧 **Sistema**          | Sunsix Linux                 |
| 🇧🇷 **Origem**         | Brasil                       |
| 📅 **Período estimado** | 2007–2008                    |
| 💿 **Mídia**            | CD-ROM                       |
| 🧬 **Base**             | Ubuntu 7.04 Feisty Fawn      |
| 🖥️ **Desktop**         | GNOME 2.18                    |
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
SHA-256: 859a058aaffb378d7a01c6420ac81a9d81f983967e4b880a7c3eb1301280b388
```

> 💡 Se você possui outra mídia do Sunsix Linux e obtiver um checksum diferente, **não descarte a cópia**. Ela pode representar uma versão ou revisão diferente e ser importante para a preservação.

---

## 🏛️ Um pedaço da história do Linux no Brasil

Durante os anos 2000, computadores vendidos no Brasil começaram a chegar ao consumidor com GNU/Linux pré-instalado como alternativa aos sistemas proprietários.

O Sunsix Linux faz parte desse período.

A distribuição foi associada a computadores de entrada e domésticos vendidos durante uma época marcada por:

* Windows XP;
* Processadores Intel Celeron, Intel Pentium e Intel Core 2 Duo;
* Memória DDR2;
* Discos Rígidos SATA;
* monitores LCD;
* CDs de instalação e recuperação;
* expansão do acesso a computadores domésticos.

O objetivo deste projeto é preservar **não apenas a ISO**, mas também o contexto em que ela existiu.

---

## 🔎 O Que Sabemos

Até o momento, a análise da mídia e das evidências disponíveis indica:

* Arquitetura **i386 / x86 32-bit**;
* Ambiente baseado na geração **Ubuntu 7.04 Feisty Fawn**;
* Desktop baseado no **GNOME 2.18**;
* Versão do Kernel: **2.6.20**
* Sistema de pacotes **APT / dpkg**;
* Personalizações visuais relacionadas à marca Sunsix;
* Distribuição em mídia **CD-ROM**;
* Compatibilidade com computadores x86 da época.

A investigação continua.

---

## 🕵️ O Que Ainda Estamos Investigando

Algumas perguntas permanecem abertas:

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

## 🖥️ Executando o Sunsix Linux

Devido à idade do sistema, a maneira mais simples de experimentá-lo atualmente é através de **virtualização ou emulação de hardware x86 antigo**.

⚠️ Compatibilidade: o sistema foi desenvolvido para hardware x86 da época. Computadores modernos podem apresentar incompatibilidades. Recomendamos QEMU ou VirtualBox.

📚 **Guias detalhados:** [`docs/troubleshooting.md`](docs/troubleshooting.md)

---

## 📸 O Sistema

Capturas do ambiente original serão adicionadas conforme a documentação avançar.

<p align="center">
  <img src="screenshots/desktop.png" alt="Desktop do Sunsix Linux" width="800">
</p>

*Desktop do Sunsix Linux — captura pendente de documentação.*

---



## 🔬 Estado da Preservação

| Item                     | Estado             |
| ------------------------ | ------------------ |
| 💿 ISO original (CD AZUL)          | ✅ Preservada       |
| ⚙️ Arquitetura           | ✅ Identificada     |
| 🖥️ Ambiente virtual     | ✅ Testável         |
| 🐧 QEMU                  | ✅ Testável         |
| 📦 VirtualBox            | ✅ Testável         |
| 📸 Screenshots           | ✅ Disponível ([`assets/screenshots/`](assets/screenshots/README.md)) |
| 📋 Lista de pacotes      | 🔄 Em análise      |
| 🎨 Customizações OEM     | 🔄 Em investigação |
| 🖥️ Hardware original    | 🔄 Em investigação |
| 🛠️ Ferramentas de análise| ✅ Disponível ([`tools/`](tools/)) |
| 📖 Documentação original | 🔍 Procurando      |
| 💿 ISO drivers e extras (CD LARANJA)   | 🔍 Procurando      |
| 🔐 SHA-256               | ✅ Confirmado     |

---

## 📚 Documentação e Ferramentas

A investigação detalhada está organizada separadamente:

* 📜 [`history.md`](docs/history.md) — contexto histórico dos PCs populares
* 🖥️ [`hardware.md`](docs/hardware.md) — especificações de hardware OEM Sunsix
* 🔬 [`technical-analysis.md`](docs/technical-analysis.md) — dossiê técnico e matriz de pacotes
* 🛠️ [`troubleshooting.md`](docs/troubleshooting.md) — guia de virtualização e problemas comuns
* 🏛️ [`preservation.md`](docs/preservation.md) — metodologia de preservação digital
* 📸 [`assets/screenshots/`](assets/screenshots/README.md) — galeria de imagens do sistema
* 🧰 [`tools/`](tools/) — scripts de automação em Python (comparação de manifestos e hashing)

---

## 🤝 Ajude a Preservar

Você possui algum material relacionado ao Sunsix?

Estamos procurando especialmente:

- 💿 CDs originais;
- 💻 Computadores Sunsix;
- 📖 Manuais e documentação;
- 📸 Fotografias;
- 💾 Drivers e CDs de recuperação;
- 📝 Relatos de quem utilizou o sistema.

Utilize nossos templates padronizados para abrir uma contribuição:
* 📜 [**Enviar um Relato Histórico**](../../issues/new?template=relato_historico.md)
* 💿 [**Submeter dados de uma Nova Mídia / CD**](../../issues/new?template=nova_midia.md)

> 🔎 Se você encontrar outra ISO, registre sua origem, tamanho e checksum antes de qualquer alteração.

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
