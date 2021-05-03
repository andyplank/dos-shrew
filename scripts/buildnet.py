from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSSwitch
from mininet.link import TCLink

class LowRateDoSTopology(Topo):
	def build(self):
		# Create Hosts h1, h2, and h3
		h1 = self.addHost('h1')
		h2 = self.addHost('h2')
		h3 = self.addHost('h3')

		# Create intermediary switch
		s1 = self.addSwitch('s1')

		# Add links from hosts to switch
		self.addLink(s1, h1, cls=TCLink, bw=10, rtt="20ms", loss=0)
		self.addLink(s1, h2, cls=TCLink, bw=10, rtt="20ms", max_queue_size=2, loss=0)
		self.addLink(s1, h3, cls=TCLink, bw=10, rtt="20ms", loss=0)

def create_topology():
	# Create an instance of the Low Rate DoS Topology
	topo = LowRateDoSTopology()

	# Create a mininet network based on the given topology
	network = Mininet(
			topo=topo,
			switch=OVSSwitch,
			autoSetMacs=True)

	# Start the network
	network.start()

	# Drop user into a mininet CLI session
	CLI(network, script="cli.sh")

	# When user exits CLI, they will end up here...
	network.stop()

if __name__ == '__main__':
	setLogLevel('info')
	create_topology()


