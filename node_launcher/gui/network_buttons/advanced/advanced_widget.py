from PySide2.QtWidgets import QWidget

from .configuration_files_layout import ConfigurationFilesLayout
from .cli_layout import CliLayout
from .ports_layout import PortsLayout
from .tls_layout import TlsLayout
from .versions_layout import VersionsLayout
from node_launcher.gui.components.grid_layout import QGridLayout
from node_launcher.gui.components.horizontal_line import HorizontalLine
from node_launcher.node_set import NodeSet


class AdvancedWidget(QWidget):
    def __init__(self, node_set: NodeSet):
        super().__init__()
        self.setWindowTitle('Advanced')
        self.node_set = node_set

        self.columns = 2

        self.layout = QGridLayout()

        self.versions_layout = VersionsLayout(node_set=node_set)
        self.ports_layout = PortsLayout(node_set=node_set)
        self.actions_layout = ConfigurationFilesLayout(node_set=node_set)
        self.cli_layout = CliLayout(node_set=self.node_set)
        self.tls_layout = TlsLayout(node_set=self.node_set)

        self.layout.addLayout(self.versions_layout, column_span=self.columns)
        self.layout.addWidget(HorizontalLine(), column_span=self.columns)
        self.layout.addLayout(self.ports_layout, column_span=self.columns)
        self.layout.addWidget(HorizontalLine(), column_span=self.columns)
        self.layout.addLayout(self.actions_layout, column_span=self.columns)
        self.layout.addWidget(HorizontalLine(), column_span=self.columns)
        self.layout.addLayout(self.cli_layout, column_span=self.columns)
        self.layout.addWidget(HorizontalLine(), column_span=self.columns)
        self.layout.addLayout(self.tls_layout, column_span=self.columns)
        self.setLayout(self.layout)
