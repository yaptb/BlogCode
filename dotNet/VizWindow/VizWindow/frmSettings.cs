/*
        Desktop Vizualation Viewer
        (c) 2016 Yet Another Pointless Tech Blog  http://yaptb.blogspot.com

*/



using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace VizWindow
{

    /// <summary>
    /// This is the settings form. It enables the user to change the application URL, transparency and save them
    /// along with the current window position and state
    /// </summary>
    public partial class frmSettings : Form
    {

        private frmMain _mainForm; 

        public frmSettings(frmMain mainForm)
        {
            InitializeComponent();

            _mainForm = mainForm;
          
        }

        
        #region Form Events

        private void btnOK_Click(object sender, EventArgs e)
        {
            this.DialogResult = DialogResult.OK;
            this.Close();

        }

        private void btnCancel_Click(object sender, EventArgs e)
        {
            this.DialogResult = DialogResult.Cancel;
            this.Close();

        }

        private void saveSettingsToolStripMenuItem_Click(object sender, EventArgs e)
        {
            SaveSettings();
        }

        private void aboutToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var frm = new frmAbout();

            frm.ShowDialog();
        }


        #endregion


        public void UpdateFormMainForm()
        {
            this.txtURL.Text = _mainForm.Browser.Address;
            this.trackBar1.Value = (int)(255.0f * _mainForm.Opacity);
        }


        private void SaveSettings()
        {
            Properties.Settings.Default.URL = this.txtURL.Text;
            Properties.Settings.Default.WindowHeight = _mainForm.Height;
            Properties.Settings.Default.WindowWidth = _mainForm.Width;
            Properties.Settings.Default.WindowPosX = _mainForm.Location.X;
            Properties.Settings.Default.WindowPosY = _mainForm.Location.Y;
            Properties.Settings.Default.WindowOpacity = this.trackBar1.Value;
            Properties.Settings.Default.WindowMaximized = _mainForm.WindowState == FormWindowState.Maximized;

            Properties.Settings.Default.Save();

            this.tsStatusLabel.Text = "Settings Saved.";

        }


        public string URL { get { return this.txtURL.Text; } }

        public int Transparency { get { return this.trackBar1.Value; } }



    }
}
