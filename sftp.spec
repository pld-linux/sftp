%define version 0.8
%define release 1
%define name sftp
%define prefix /usr

Summary: sftp: a ftp-replacement over an rsh/ssh tunnel
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Applications/Internet
Source: sftp-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-root
Url: http://www.xbill.org/sftp
Packager: Brian Wellington <bwelling@xbill.org>

%description
sftp is an ftp replacement that runs over an ssh tunnel. Two programs
are included - sftp and sftpserv. When sftp is run and a host is
connected to (either by running 'sftp remotehost' or 'open remotehost'
from the sftp prompt), an ssh connection is initiated to the remote
host, and sftpserv is run.

From within sftp, all of the normal ftp commands are present: open,
close, get, put, pwd, cd, ls, lcd, quit, etc. There's also exec, which runs
a program on the remote end.

%changelog
* Mon Feb 14 2000 Brian Wellington <bwelling@xbill.org>
- updated to 0.8
- use make install now

* Tue Jan 11 2000 Brian Wellington <bwelling@xbill.org>
- updated to 0.7

* Wed Dec 28 1999 Brian Wellington <bwelling@xbill.org>
- updated to 0.6

* Sun Dec 26 1999 Brian Wellington <bwelling@xbill.org>
- updated to 0.5

* Fri Nov 26 1999 Chris Green <sprout@dok.org>
- updated to 0.4

* Mon Nov 22 1999 Chris Green <sprout@dok.org>
- created spec

%prep
rm -rf $RPM_BUILD_ROOT
%setup

%build
./configure --prefix=%{prefix} 
make CFLAGS="$RPM_OPT_FLAGS" 


%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/man/man1
make ROOT="$RPM_BUILD_ROOT" install

%files
%defattr(-,root,root)
%doc README Changelog
/usr/bin/sftp
/usr/bin/rsftp
/usr/bin/sftpserv
/usr/man/man1/sftp.1

%clean
rm -rf $RPM_BUILD_ROOT 

# end of file
