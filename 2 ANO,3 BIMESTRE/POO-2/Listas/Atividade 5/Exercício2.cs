/* *******************************************************************
* Colegio Técnico Antônio Teixeira Fernandes (Univap)
* Curso Técnico em Informática - Data de Entrega: 14/08/2020
* Autores do Projeto: Laurent Chaves Assis Feliciano
* Turma: 2F-Informática
* Atividade 5
* Observação: nenhuma
* Exercício2.cs
* ************************************************************/
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Forms
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            textBox5.Clear();
            int Dia= int.Parse(textBox1.Text);
            int Mes = int.Parse(textBox2.Text);
            int Ano = int.Parse(textBox3.Text);
            DateTime Data = new DateTime(Ano, Mes, Dia);
            int N = int.Parse(textBox4.Text);
            textBox2.Clear();
            int C = 0;
            for (C=1;C<=N;C++)
            {
                Data = Data.AddDays(150);
                textBox5.AppendText(Data.ToString("dd-MM-yy") + Environment.NewLine);
            }
        }
    }
}
