 /* *******************************************************************
 * Colegio Técnico Antônio Teixeira Fernandes (Univap)
 * Curso Técnico em Informática - Data de Entrega: 14/08/2020
 * Autores do Projeto: Laurent Chaves Assis Feliciano
 * Turma: 2F-Informática
 * Atividade 5
 * Observação: nenhuma
 * Exercício1.cs
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
            int Dia = int.Parse(textBox1.Text);
            int Mes = int.Parse(textBox2.Text);
            int Ano = int.Parse(textBox3.Text);
            DateTime Data = new DateTime(Ano, Mes, Dia);
            int AnoInicial = int.Parse(textBox4.Text);
            int AnoFinal = int.Parse(textBox5.Text);
            textBox4.Clear();
            textBox5.Clear();
            if(Data.Year > AnoFinal)
                MessageBox.Show("Sua data de nascimento veio depois do Ano Final, Digite novamente.");
            if(AnoInicial > AnoFinal
                MessageBox.Show("Ano Inicial veio após Ano Final, Digite novamente.");
            for (DateTime Aniversario = new DateTime(AnoInicial, Mes, Dia);Aniversario.Year <= AnoFinal; Aniversario = Aniversario.AddYears(++))
            {
                textBox6.AppendText(Aniversario.ToString("yyyy")+" - "+ Aniversario.ToString("dddd")+Environment.NewLine);
                textBox6.AppendText(Environment.NewLine);
            }
        }
    }
}
