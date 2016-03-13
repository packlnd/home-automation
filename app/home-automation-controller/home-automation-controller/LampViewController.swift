//
//  FirstViewController.swift
//  home-automation-controller
//
//  Created by Patrik Ackland on 3/12/16.
//  Copyright © 2016 Patrik Ackland. All rights reserved.
//

import UIKit
import Alamofire

class LampViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    @IBAction func onOffSwitch(sender: UISwitch) {
        print("It's " + sender.on.description + "!")
    }
}