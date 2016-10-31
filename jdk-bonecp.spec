Name     : jdk-bonecp
Version  : 0.8.0.RELEASE
Release  : 4
URL      : https://repo1.maven.org/maven2/com/jolbox/bonecp/0.8.0.RELEASE/bonecp-0.8.0.RELEASE.jar
Source0  : https://repo1.maven.org/maven2/com/jolbox/bonecp/0.8.0.RELEASE/bonecp-0.8.0.RELEASE.jar
Source1  : https://repo1.maven.org/maven2/com/jolbox/bonecp/0.8.0.RELEASE/bonecp-0.8.0.RELEASE.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-bonecp-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-bonecp package.
Group: Data

%description data
data components for the jdk-bonecp package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/bonecp.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/bonecp.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/bonecp.xml \
%{buildroot}/usr/share/maven-poms/bonecp.pom \
%{buildroot}/usr/share/java/bonecp.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/bonecp.jar
/usr/share/maven-metadata/bonecp.xml
/usr/share/maven-poms/bonecp.pom
