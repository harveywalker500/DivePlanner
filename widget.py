import sys
from formulas.o2_table_generator import *
from formulas import common as c
from formulas import metric as m
from formulas import imperial as i

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem

from ui_form import Ui_Widget


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.show_warning()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Connect the calculate button to the function
        self.ui.O2Table_CalculateButton.clicked.connect(self.calculate_o2_tables)
        self.ui.EAD_CalculateButton.clicked.connect(self.calculate_ead_metric)
        self.ui.MD_CalculateButton.clicked.connect(self.calculate_md_metric)
        self.ui.SAC_CalculateButton.clicked.connect(self.calculate_SAC_metric)
        self.ui.GRE_CalculateButton.clicked.connect(self.calculate_GRE_metric)
        self.ui.AGS_CalculateButton.clicked.connect(self.calculate_AGS_metric)
        self.ui.AT_CalculateButton.clicked.connect(self.calculate_AT_metric)
        self.ui.TP_CalculateButton.clicked.connect(self.calculate_TP_metric)

    def show_warning(self):
        warning_text = (
            "While every effort has been made to ensure the accuracy and completeness of the "
            "dive planning information provided, it is crucial for divers to always exercise caution "
            "and use their training, experience, and judgment. Diving conditions can change rapidly, "
            "and individual tolerances may vary. Always prioritize safety and consult with experienced "
            "dive professionals when planning and executing dives."
        )

        QMessageBox.warning(self, "WARNING: Please read before continuing.", warning_text)

    def calculate_o2_tables(self):
        if self.ui.O2Table_metricRadioButton.isChecked():
            unit_type = "metric"
        elif self.ui.O2Table_imperialRadioButton.isChecked():
            unit_type = "imperial"
        else:
            QMessageBox.warning(self, "Error!", "Please check either metric or imperial.")
            return 0;

        o2_fraction = float(self.ui.O2Table_o2ComboBox.currentText()) / 100

        if unit_type == "metric":
            data = calculate_table_for_o2_fraction_metric(o2_fraction)
        else:
            data = calculate_table_for_o2_fraction_imperial(o2_fraction)

        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['Depth', 'EAD', 'PO2', 'OTU/min'])

        for i in range(len(data['Depth'])):
            depth_item = QStandardItem(str(data['Depth'][i]))
            ead_item = QStandardItem(str(data['EAD'][i]))
            po2_item = QStandardItem(str(data['PO2'][i]))
            otu_min_item = QStandardItem(str(data['OTU/min'][i]))
            model.appendRow([depth_item, ead_item, po2_item, otu_min_item])

            self.ui.O2Table_ResultTable.setModel(model)
            self.ui.O2Table_ResultTable.verticalHeader().hide()

    def calculate_ead_metric(self):
        depth = float(self.ui.EAD_DepthField.text())
        o2_fraction = float(self.ui.EAD_O2ComboBox.currentText()) / 100

        result = m.ead(o2_fraction, depth)

        self.ui.EAD_ResultLabel.setText(f"EAD: {result: .2f}m")

    def calculate_md_metric(self):
        o2_fraction = float(self.ui.MD_O2ComboBox.currentText()) / 100

        if self.ui.MD_14.isChecked():
            result = m.max_depth_bottom(o2_fraction)
            self.ui.MD_ResultLabel.setText(f"Max Depth for 1.4PPO2: {result: .2f}m")

        elif self.ui.MD_16.isChecked():
            result = m.max_depth_deco(o2_fraction)
            self.ui.MD_ResultLabel.setText(f"Max Depth for 1.6PPO2: {result: .2f}m")


    def calculate_SAC_metric(self):
        bar = float(self.ui.SAC_BarField.text())
        cylinder = float(self.ui.SAC_CylinderField.text())
        if self.ui.SAC_DoubleCheckbox.isChecked():
            cylinder = cylinder * 2

        depth = float(self.ui.SAC_DepthField.text())
        time = float(self.ui.SAC_TimeField.text())
        result = m.sac_rate(bar, cylinder, depth, time)

        self.ui.SAC_ResultLabel.setText(f"SAC Rate: {result: .2f} L/Min")

    def calculate_GRE_metric(self):
        time = float(self.ui.GRE_TimeField.text())
        sac = float(self.ui.GRE_SACField.text())
        depth = float(self.ui.GRE_DepthField.text())

        result = m.gas_requirement_estimate(time, sac, depth)

        self.ui.GRE_ResultLabel.setText(f"Required Gas: {result: .2f}L")

    def calculate_AGS_metric(self):
        volume = float(self.ui.AGS_VolumeField.text())
        bar = float(self.ui.AGS_BarField.text())

        result = m.actual_gas_supply(volume, bar)

        self.ui.AGS_ResultLabel.setText(f"Actual Gas Supply: {result: .2f}L")

    def calculate_AT_metric(self):
        bottom = float(self.ui.AT_BottomDepthField.text())
        stop = float(self.ui.AT_StopDepthField.text())
        ascent = float(self.ui.AT_AscentRateField.text())

        result = m.ascent_time(bottom, stop, ascent)

        self.ui.AT_ResultLabel.setText(f"Ascent Time: {result: .2f} mins")

    def calculate_TP_metric(self):
        start = float(self.ui.TP_StartPressureField.text())
        bottom = float(self.ui.TP_BottomDepthField.text())
        cylinder = float(self.ui.TP_CylinderField.text())

        result = m.turn_pressure(start, bottom, cylinder)

        self.ui.TP_ResultLabel.setText(f"Turn Pressure: {result: .2f} bar")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
