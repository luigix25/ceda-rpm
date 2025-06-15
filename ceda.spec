Name:           ceda-cemu
Version:        1.0.0
Release:        %autorelease
Summary:        ceda-cemu

License:        MIT
URL:            https://github.com/GLGPrograms/ceda-cemu
Source:         ceda-cemu.tar.xz
Source:         CGV7.2_ROM.bin
Source:         V1.01_ROM.bin
Source:         ceda-cemu.ini

ExclusiveArch: x86_64

BuildRequires: make gcc g++ cmake
BuildRequires: SDL2-devel SDL2_mixer-devel

Patch: 0001-remove-tidy.patch
Patch: 0001-fix-path-configurazione.patch
Patch: 0001-serial.c-Check-for-sockfd-value.patch

%description
ceda-cemu is an emulator of very fancy and powerful machine

%prep
%autosetup -n ceda-cemu -p1

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build --target ceda

%install
mkdir -p %{buildroot}%{_datadir}/%{name}/rom
mkdir -p %{buildroot}%{_bindir}/

#install the ini file
install %{_sourcedir}/ceda-cemu.ini %{buildroot}%{_datadir}/%{name}/

#install rom
install %{_sourcedir}/*.bin %{buildroot}%{_datadir}/%{name}/rom/

#install binary
install \
  -m 755 \
  ./redhat-linux-build/ceda \
  %{buildroot}%{_bindir}/ceda

%files
%{_bindir}/ceda
%{_datadir}/%{name}/rom/*.bin
%{_datadir}/%{name}/ceda-cemu.ini

%doc README.md

%changelog
%autochangelog
