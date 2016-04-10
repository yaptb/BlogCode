namespace VizWindow
{
    partial class frmMain
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(frmMain));
            this.niNotificationIcon = new System.Windows.Forms.NotifyIcon(this.components);
            this.cmNotificaitonContextMenu = new System.Windows.Forms.ContextMenuStrip(this.components);
            this.tsInteractive = new System.Windows.Forms.ToolStripMenuItem();
            this.tsSettings = new System.Windows.Forms.ToolStripMenuItem();
            this.cmNotificaitonContextMenu.SuspendLayout();
            this.SuspendLayout();
            // 
            // niNotificationIcon
            // 
            this.niNotificationIcon.ContextMenuStrip = this.cmNotificaitonContextMenu;
            this.niNotificationIcon.Icon = ((System.Drawing.Icon)(resources.GetObject("niNotificationIcon.Icon")));
            this.niNotificationIcon.Text = "VizWindow";
            this.niNotificationIcon.Visible = true;
            // 
            // cmNotificaitonContextMenu
            // 
            this.cmNotificaitonContextMenu.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.tsInteractive,
            this.tsSettings});
            this.cmNotificaitonContextMenu.Name = "contextMenuStrip1";
            this.cmNotificaitonContextMenu.Size = new System.Drawing.Size(153, 70);
            // 
            // tsInteractive
            // 
            this.tsInteractive.Checked = true;
            this.tsInteractive.CheckOnClick = true;
            this.tsInteractive.CheckState = System.Windows.Forms.CheckState.Checked;
            this.tsInteractive.Name = "tsInteractive";
            this.tsInteractive.Size = new System.Drawing.Size(152, 22);
            this.tsInteractive.Text = "Interactive";
            this.tsInteractive.Click += new System.EventHandler(this.tsInteractive_Click);
            // 
            // tsSettings
            // 
            this.tsSettings.Name = "tsSettings";
            this.tsSettings.Size = new System.Drawing.Size(152, 22);
            this.tsSettings.Text = "Settings";
            this.tsSettings.Click += new System.EventHandler(this.settingsToolStripMenuItem_Click);
            // 
            // frmMain
            // 
            this.ClientSize = new System.Drawing.Size(620, 588);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "frmMain";
            this.Opacity = 0.5D;
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.frmMain_FormClosing);
            this.Load += new System.EventHandler(this.frmMain_Load);
            this.cmNotificaitonContextMenu.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.NotifyIcon niNotificationIcon;
        private System.Windows.Forms.ContextMenuStrip cmNotificaitonContextMenu;
        private System.Windows.Forms.ToolStripMenuItem tsInteractive;
        private System.Windows.Forms.ToolStripMenuItem tsSettings;
    }
}

