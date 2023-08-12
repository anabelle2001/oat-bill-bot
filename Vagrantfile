Vagrant.configure("2") do |config|
  config.vm.box = "generic/ubuntu2204"

  config.vm.provider :libvirt do |libvirt|
    libvirt.memory = "1024"
    libvirt.cpus = 1
    libvirt.graphics_type = "none"
  endq

  # These settings are for me 
  # they will probably cause probems for you
  # feel free to delete them.
  config.vm.network(
    :public_network,
    :dev => "br0",
    :mode => "bridge",
    :type => "bridge"
  )

  # config.vm.define "sql-database" do |machine|
  #   machine.vm.provision "ansible" do |ansible|
  #     ansible.playbook="./ansible/sql/MAIN.yml"
  #   end
  # end
  
  # config.vm.provision "ansible" do |ansible|
  #   ansible.playbook = "./ansible/common/MAIN.yml"
  # end

end
