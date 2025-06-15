NAME := ceda-cemu
VERSION ?= 0.1
URL := https://github.com/GLGPrograms/ceda-cemu
ROM1 := https://github.com/GLGPrograms/ceda-home/raw/refs/heads/main/assets/v1.01_rom.bin
ROM2 := https://github.com/GLGPrograms/ceda-home/raw/refs/heads/main/assets/cgv7.2_rom.bin
ROM3 := https://github.com/GLGPrograms/ceda-home/raw/refs/heads/main/assets/cgv7.2_rom.bin

.PHONY: all clean down-src down-rom

all: down-src down-rom clean

down-src:
	@echo Downloading version $(VERSION)
	git clone $(URL) $(NAME) --single-branch --depth=1 && \
	pushd $(NAME) && \
	git submodule update --init --depth 1 && \
	popd && \
	tar Jcf $(NAME).tar.xz $(NAME) && \
	sha512sum $(NAME).tar.xz

down-rom:
	wget $(ROM1) -O V1.01_ROM.bin && \
	wget $(ROM2) -O CGV7.2_ROM.bin && \
	sha512sum *bin

clean:
	rm -rf $(NAME)