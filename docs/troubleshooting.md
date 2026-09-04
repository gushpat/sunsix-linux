# 🛠️ Guia de Virtualização e Resolução de Problemas — Sunsix Linux

> **Instruções para executar o Sunsix Linux (Ubuntu 7.04 Feisty Fawn i386) em máquinas virtuais modernas e resolver problemas comuns de compatibilidade.**

---

## ⚠️ Recomendações de Segurança

* **Não utilize como sistema operacional principal.**
* O Sunsix Linux utiliza pacotes e kernel de 2007 (Linux 2.6.20) sem atualizações de segurança.
* Execute **sempre em ambiente isolado (VirtualBox / QEMU)** e com a placa de rede **desativada ou desconectada da Internet**.

---

## 📦 1. Requisitos do Sistema para Virtualização

| Recurso           | Valor Recomendado                            |
| ----------------- | -------------------------------------------- |
| **Arquitetura**   | i386 / x86 32-bit                            |
| **Memória RAM**   | 512 MB a 1024 MB                             |
| **Disco Rígido**  | 8 GB a 10 GB (formato VDI, QCOW2 ou VMDK)    |
| **Controladora**  | IDE ou SATA em modo de compatibilidade legada|
| **Vídeo**         | VBoxVGA ou Standard VGA (sem aceleração 3D)  |

---

## 🖥️ 2. Executando no VirtualBox (Versão 7.x ou Superior)

### Passo a Passo de Criação da VM:

1. Clique em **Novo** no VirtualBox.
2. Defina os parâmetros principais:
   * **Nome:** `Sunsix Linux (2007)`
   * **Tipo:** `Linux`
   * **Versão:** `Ubuntu (32-bit)`
3. **Memória RAM:** Selecione `512 MB` ou `1024 MB`. *(Evite atribuir mais de 2 GB de RAM para sistemas 32-bit legados).*
4. **Disco Rígido:** Crie um novo disco virtual de `10 GB` (VDI, alocado dinamicamente).
5. **Ajustes nas Configurações da VM:**
   * **Sistema -> Processador:** 1 CPU (ativar PAE/NX se necessário).
   * **Monitor -> Tela:**
     * Memória de Vídeo: `32 MB` ou `64 MB`.
     * Controladora Gráfica: Escolha **VBoxVGA** (caso haja aviso do VirtualBox, desconsidere para sistemas antigos).
     * **Desative** "Habilitar Aceleração 3D".
   * **Armazenamento:**
     * Selecione o leitor de CD/DVD virtual e carregue a ISO do `sunsix-linux.iso`.
   * **Rede:** Altere o adaptador de rede para "Desconectado" ou "NAT" com o cabo desconectado.

---

## 🐧 3. Executando no QEMU

O QEMU oferece excelente emulação de hardware x86 clássico para sistemas dessa época.

### Comando de Execução Rápida (Live CD):

```bash
qemu-system-i386 \
  -m 512M \
  -cdrom sunsix-linux.iso \
  -vga std \
  -net nic,model=pcnet \
  -net user \
  -boot d
```

### Comando para Instalação em Disco Virtual:

```bash
# 1. Criar imagem de disco de 10GB
qemu-img create -f qcow2 sunsix-disk.qcow2 10G

# 2. Iniciar VM com a ISO e o disco criado
qemu-system-i386 \
  -m 512M \
  -hda sunsix-disk.qcow2 \
  -cdrom sunsix-linux.iso \
  -vga std \
  -boot d
```

---

## 🔧 4. Resolução de Problemas Comuns (Troubleshooting)

### 🔴 1. Kernel Panic ou Travamento no Boot
* **Sintoma:** O boot congela na inicialização do kernel 2.6.20 ou exibe erros de temporizador APIC/ACPI.
* **Solução:** No menu de boot do Live CD (ISOLinux), pressione `F6` (Opções) ou edite a linha de boot adicionando os seguintes parâmetros:
  ```text
  acpi=off noapic nolapic
  ```

### 🔴 2. Tela Preta ao Iniciar o Ambiente Gráfico (X.Org)
* **Sintoma:** O boot conclui a etapa em texto, mas a tela fica preta ou distorcida ao carregar o GNOME 2.18.
* **Solução:** 
  * Certifique-se de que a controladora gráfica da VM está definida como **VBoxVGA** (VirtualBox) ou **std** (QEMU).
  * Adicione o parâmetro `xforcevesa` nas opções de boot da ISO para forçar o driver VESA genérico.

### 🔴 3. Resolução de Tela Limitada a 800x600
* **Sintoma:** Não é possível alterar a resolução no GNOME para 1024x768 ou superior.
* **Causa:** Ausência dos módulos do Guest Additions modernos compatíveis com o Kernel 2.6.20 e X.Org 7.2.
* **Solução:** Edite manualmente o arquivo `/etc/X11/xorg.conf` dentro da máquina virtual para adicionar resoluções suportadas pela seção `Display`.

### 🔴 4. Erros ao tentar usar o APT / Repositórios Offline
* **Sintoma:** `apt-get update` falha com erro 404 ao tentar acessar `archive.ubuntu.com`.
* **Causa:** O Ubuntu 7.04 (Feisty Fawn) atingiu o Fim da Vida Útil (EOL) em outubro de 2008 e seus repositórios foram movidos para o servidor oficial de arquivos antigos.
* **Solução:** Caso queira instalar pacotes históricos, atualize o arquivo `/etc/apt/sources.list` substituindo o domínio dos repositórios por:
  ```text
  http://old-releases.ubuntu.com/ubuntu/ feisty main restricted universe multiverse
  http://old-releases.ubuntu.com/ubuntu/ feisty-updates main restricted universe multiverse
  ```

---

## 📚 Referências e Links Relacionados

* 🔬 [`technical-analysis.md`](technical-analysis.md) — Dossiê técnico e análise da ISO
* 🖥️ [`hardware.md`](hardware.md) — Especificações de hardware OEM Sunsix
* 🏛️ [`preservation.md`](preservation.md) — Metodologia de preservação digital
