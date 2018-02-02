#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : shim
Version  : 12
Release  : 10
URL      : https://github.com/rhboot/shim/releases/download/12/shim-12.tar.bz2
Source0  : https://github.com/rhboot/shim/releases/download/12/shim-12.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
BuildRequires : gnu-efi
BuildRequires : gnu-efi-dev
BuildRequires : nss-bin
BuildRequires : openssl-dev
BuildRequires : pesign
BuildRequires : util-linux
Patch1: 0001-Add-Intel-Certificate.patch
Patch2: 0002-Fix-security-policy-compile-errors.patch

%description
shim is a trivial EFI application that, when run, attempts to open and
execute another application. It will initially attempt to do this via the
standard EFI LoadImage() and StartImage() calls. If these fail (because secure
boot is enabled and the binary is not signed with an appropriate key, for
instance) it will then validate the binary against a built-in certificate. If
this succeeds and if the binary or signing key are not blacklisted then shim
will relocate and execute the binary.

%prep
%setup -q -n shim-12
%patch1 -p1
%patch2 -p1

openssl x509 -in clear-linux-sb.pem -out clear-linux-sb.cer -outform der

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1510730040
make V=1  %{?_smp_mflags} EFI_CRT_OBJS=/usr/lib64/crt0-efi-x86_64.o DEFAULT_LOADER=loaderx64.efi VENDOR_CERT_FILE=clear-linux-sb.cer OVERRIDE_SECURITY_POLICY=1

%install
export SOURCE_DATE_EPOCH=1510730040
rm -rf %{buildroot}
true
## make_install_append content
mkdir -p %{buildroot}/usr/lib/shim
/usr/bin/install -p -D -m 0755 shimx64.efi %{buildroot}/usr/lib/shim/shimx64.efi
/usr/bin/install -p -D -m 0755 mmx64.efi.signed %{buildroot}/usr/lib/shim/mmx64.efi
/usr/bin/install -p -D -m 0755 fbx64.efi.signed %{buildroot}/usr/lib/shim/fbx64.efi
## make_install_append end

%files
%defattr(-,root,root,-)
/usr/lib/shim/fbx64.efi
/usr/lib/shim/mmx64.efi
/usr/lib/shim/shimx64.efi
