#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Digest-SHA1
Version  : 2.13
Release  : 10
URL      : https://cpan.metacpan.org/authors/id/G/GA/GAAS/Digest-SHA1-2.13.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GA/GAAS/Digest-SHA1-2.13.tar.gz
Summary  : Perl interface to the SHA-1 algorithm
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Digest-SHA1-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
The Digest::SHA1 module allows you to use the NIST SHA-1 message
digest algorithm from within Perl programs.  The algorithm takes as
input a message of arbitrary length and produces as output a 160-bit
"fingerprint" or "message digest" of the input.

%package dev
Summary: dev components for the perl-Digest-SHA1 package.
Group: Development
Provides: perl-Digest-SHA1-devel = %{version}-%{release}
Requires: perl-Digest-SHA1 = %{version}-%{release}

%description dev
dev components for the perl-Digest-SHA1 package.


%package perl
Summary: perl components for the perl-Digest-SHA1 package.
Group: Default
Requires: perl-Digest-SHA1 = %{version}-%{release}

%description perl
perl components for the perl-Digest-SHA1 package.


%prep
%setup -q -n Digest-SHA1-2.13
cd %{_builddir}/Digest-SHA1-2.13

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Digest::SHA1.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Digest/SHA1.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Digest/SHA1/SHA1.so
