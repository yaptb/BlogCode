/*
        Desktop Vizualation Viewer
        (c) 2016 Yet Another Pointless Tech Blog  http://yaptb.blogspot.com

        This application wraps the https://github.com/cefsharp/CefSharp browser in a transparent window to enable animated web based desktops
*/



using System;
using System.Drawing;
using System.Windows.Forms;
using CefSharp;
using CefSharp.WinForms;
using VizWindow.Properties;

namespace VizWindow
{

    /// <summary>
    /// this is the main form. It simply hosts the browser control and the notify icon
    /// </summary>
    public partial class frmMain : Form
    {


        public frmMain()
        {
            InitializeComponent();
            this.AllowTransparency = true;

            SettingsDialog = new frmSettings(this);
        }


        #region Form Events

        private void frmMain_Load(object sender, EventArgs e)
        {

            RestoreSavedSettings();
            InitializeBrowserControl();
        
        }
        
        
        private void frmMain_FormClosing(object sender, FormClosingEventArgs e)
        {
            ShutdownBrowserControl();
        }
        

        private void tsInteractive_Click(object sender, EventArgs e)
        {
            if (this.tsInteractive.Checked)
                SetInteractiveMode();
            else

                SetBackgroundMode();
        }


        private void settingsToolStripMenuItem_Click(object sender, EventArgs e)
        {

            SettingsDialog.UpdateFormMainForm();

            if (SettingsDialog.ShowDialog() == DialogResult.OK)
                UpdateSettingsFromDialog();
        }


        #endregion


        /// <summary>
        /// start up the embedded browser control
        /// </summary>
        private void InitializeBrowserControl()
        {
            Cef.Initialize();
            Browser = new ChromiumWebBrowser(Url);
            this.Controls.Add(Browser);
        }


        /// <summary>
        /// shutdown the browser control to free unmanaged resources
        /// </summary>
        private void ShutdownBrowserControl()
        {
            Cef.Shutdown();
        }


        /// <summary>
        /// sets the application to interactive mode, where the user can interact with the browser
        /// </summary>
        private void SetInteractiveMode()
        {

            this.FormBorderStyle = FormBorderStyle.Sizable;
            this.Browser.Enabled = true;
        }




        /// <summary>
        /// sets the application to background mode, where input events are ignored 
        /// </summary>
        private void SetBackgroundMode()
        {
            //we are in background mode

            this.Browser.Enabled = false;

            this.FormBorderStyle = FormBorderStyle.None;

            if (this.WindowState == FormWindowState.Maximized)
            {

                //HACK: fix the issue where removing borders from a maximized window bleeds the screen into other monitors
                //by forcing the window out of maximized mode when non-interactive and resizing to the screen bounds
                //TODO: put the window back into mazimized mode 
                this.WindowState = FormWindowState.Normal;

                Screen screen = Screen.FromControl(this);
                this.Location = screen.WorkingArea.Location;
                this.Width = screen.WorkingArea.Width;
                this.Height = screen.Bounds.Height;
            }

        }



        /// <summary>
        /// restore a user's previously saved settings
        /// </summary>
        private void RestoreSavedSettings()
        {

            //restore previsiouly saved settings
            var winX = Settings.Default.WindowPosX;
            var winY = Settings.Default.WindowPosY;
            var winH = Settings.Default.WindowHeight;
            var winW = Settings.Default.WindowWidth;
            var isMaximized = Settings.Default.WindowMaximized;
            var Url = Settings.Default.URL;


            this.Width = winW;
            this.Height = winH;
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point(winX, winY);
            this.Opacity = (float)(Settings.Default.WindowOpacity) / 255.0f;

            if (isMaximized)
                this.WindowState = FormWindowState.Maximized;

        }


        /// <summary>
        /// update the current settings from the ones the users have specified on the settings dialog
        /// </summary>
        private void UpdateSettingsFromDialog()
        {
            this.Opacity = (float)(SettingsDialog.Transparency) / 255.0f;

            if (SettingsDialog.URL != Browser.Address)
            {
                //navigate to a new address 
                Url = SettingsDialog.URL;
                this.Browser.Load(Url);

            }
        }



        public ChromiumWebBrowser Browser { get; set; }

        public string Url { get; set; }

        private frmSettings SettingsDialog { get; set; }
    }
}