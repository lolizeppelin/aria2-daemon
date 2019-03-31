%global debug_package %{nil}
%define _release 1

Name:           aria2-daemon
Version:        1.0.0
Release:        %{_release}%{?dist}
Summary:        ddns utils
Group:          Development/Libraries
License:        MPLv1.1 or GPLv2
URL:            http://github.com/Lolizeppelin/%{name}
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch


Requires:       aria2 >= 2.7
Requires:       jellyfin >= 10.0


%description
Aria2 rpc daemon service

%prep
%setup -q -n %{name}-%{version}


%install
mkdir -p %{buildroot}%{_sharedstatedir}/aria2d
mkdir -p %{buildroot}%{_datarootdir}/aria2d

%{__install} -D -m 0644 -p aria2d.service %{buildroot}%{_unitdir}/aria2d.service
%{__install} -D -m 0644 -p etc/aria2d/aria2d.conf -t %{buildroot}%{_sysconfdir}/aria2d
copy -r ariang %{buildroot}%{_datarootdir}/aria2d/

%preun
systemctl stop aria2d.service


%files
%defattr(-,root,root,-)
%{_unitdir}/aria2d.service
%{buildroot}%{_datarootdir}/aria2d
%doc etc/nginx/aria2d.conf
%defattr(-,jellyfin,jellyfin,-)
%dir %{_sharedstatedir}/aria2d
%config(noreplace) %{_sysconfdir}/aria2d/aria2d.conf


%changelog
* Fri Mar 15 2019 Lolizeppelin <lolizeppelin@gmail.com> - 1.0.0
- Initial Package